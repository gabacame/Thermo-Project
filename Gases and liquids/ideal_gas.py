import matplotlib.pyplot as plt
import numpy as np
import json
import os

class BoyleLaw:
    
    def __init__(self, P1=None, V1=None, P2=None, V2=None, k=None):
        self.P1 = P1
        self.V1 = V1
        self.P2 = P2
        self.V2 = V2
        self.k = k
    
    def calculate(self):
        if self.k:
            if self.P1:
                self.V1 = self.k / self.P1
                return self.V1
            elif self.V1:
                self.P1 = self.k / self.V1
                return self.P1
        else:
            # If P1, V1 and P2 are known -> calculate V2
            if self.P1 is not None and self.V1 is not None and self.P2 is not None and self.V2 is None:
                self.V2 = (self.P1 * self.V1) / self.P2
                return self.V2
            
            # If P1, V1 and V2 are known -> calculate P2
            elif self.P1 is not None and self.V1 is not None and self.P2 is None and self.V2 is not None:
                self.P2 = (self.P1 * self.V1) / self.V2
                return self.P2
            
            # If V1, P2 and V2 are known -> calculate P1
            elif self.P1 is None and self.V1 is not None and self.P2 is not None and self.V2 is not None:
                self.P1 = (self.P2 * self.V2) / self.V1
                return self.P1
            
            # If P1, P2 and V2 are known -> calculate V1
            elif self.P1 is not None and self.V1 is None and self.P2 is not None and self.V2 is not None:
                self.V1 = (self.P2 * self.V2) / self.P1
                return self.V1
            
            else:
                raise ValueError("Exactly three values must be provided to calculate the fourth.")
        
    def plot_isotherm(self, P1, V1, pressure_range):
        volumes = [(P1 * V1) / P for P in pressure_range]
        plt.plot(volumes, pressure_range)
        plt.xlabel('Volume (L)')
        plt.ylabel('Pressure (atm)')
        plt.title('Isotherm of Boyle')
        plt.grid(True)
        plt.show()

    def plot_isotherm_from_k(self, k, value_range, known='P'):
        if known == 'P':
            pressures = value_range
            volumes = [k / P for P in pressures]
        elif known == 'V':
            volumes = value_range
            pressures = [k / V for V in volumes]
        else:
            raise ValueError("'known' should be either 'P' or 'V'")
        
        plt.plot(volumes, pressures)
        plt.xlabel('Volume (L)')
        plt.ylabel('Pressure (atm)')
        plt.title('Isotherm of Boyle with k = {}'.format(k))
        plt.grid(True)
        plt.show()

class CharlesLaw:
    
    def __init__(self, V1=None, T1=None, V2=None, T2=None, k=None):
        self.V1 = V1
        self.T1 = T1
        self.V2 = V2
        self.T2 = T2
        self.k = k

    def calculate(self):
        if self.k:
            if self.V1:
                self.T1 = self.k / self.V1
                return self.T1
            elif self.T1:
                self.V1 = self.k / self.T1
                return self.V1
        else:
            # If V1, T1 and V2 are known -> calculate T2
            if self.V1 is not None and self.T1 is not None and self.V2 is not None and self.T2 is None:
                self.T2 = (self.V2 * self.T1) / self.V1
                return self.T2
            
            # If V1, T1 and T2 are known -> calculate V2
            elif self.V1 is not None and self.T1 is not None and self.V2 is None and self.T2 is not None:
                self.V2 = (self.V1 * self.T2) / self.T1
                return self.V2
            
            # If V2, T1 and T2 are known -> calculate V1
            elif self.V1 is None and self.T1 is not None and self.V2 is not None and self.T2 is not None:
                self.V1 = (self.V2 * self.T1) / self.T2
                return self.V1
            
            # If V1, V2 and T2 are known -> calculate T1
            elif self.V1 is not None and self.V2 is not None and self.T1 is None and self.T2 is not None:
                self.T1 = (self.V1 * self.T2) / self.V2
                return self.T1
            
            else:
                raise ValueError("Exactly three values must be provided to calculate the fourth.")
    
    def plot_isobar(self, V1, T1, temperature_range):
        volumes = [(V1 * (T + 273.15)) / T1 for T in temperature_range]
        plt.plot([T + 273.15 for T in temperature_range], volumes)  # Convertimos la temperatura a Kelvin también en el eje x
        plt.xlabel('Temperature (K)')
        plt.ylabel('Volume (L)')
        plt.title('Isobar of Charles')
        plt.grid(True)
        plt.show()

    def plot_isobar_from_k(self, k, value_range, known='V'):
        if known == 'V':
            volumes = value_range
            temperatures = [k / V for V in volumes]
        elif known == 'T':
            temperatures = value_range
            volumes = [k * T for T in temperatures]
        else:
            raise ValueError("'known' should be either 'V' or 'T'")
        
        plt.plot(temperatures, volumes)
        plt.xlabel('Temperature (K)')
        plt.ylabel('Volume (L)')
        plt.title('Isobar of Charles with k = {}'.format(k))
        plt.grid(True)
        plt.show()

class IdealGasLaw(BoyleLaw, CharlesLaw):
    
    def __init__(self, P=None, V=None, T=None, n=None, R_unit=None):
        self.P = P
        self.V = V
        self.T = T
        self.n = n
        self.R_unit = R_unit  # La unidad de la constante R
        self.R = self.get_R(R_unit)  # Obtener el valor de la constante R
    
    def get_R(self, unit):
        # Obtener la ruta al directorio actual
        current_dir = os.path.dirname(__file__)
        
        # Crear la ruta al archivo R.json
        file_path = os.path.join(current_dir, 'R.json')
        
        # Leer el archivo JSON y obtener el valor de la constante R
        with open(file_path, 'r') as file:
            R_values = json.load(file)
        return R_values.get(unit, None)  # Devuelve None si la unidad no está en el archivo
    
    def calculate(self, param_to_find):
        # Asegurarse de que se proporcionen suficientes datos
        if None in [self.P, self.V, self.T, self.n, self.R] and param_to_find not in ['P', 'V', 'T', 'n']:
            raise ValueError("Insufficient data to perform calculation")
        
        if param_to_find == 'P':
            self.P = (self.n * self.R * self.T) / self.V
            return self.P
        elif param_to_find == 'V':
            self.V = (self.n * self.R * self.T) / self.P
            return self.V
        elif param_to_find == 'T':
            self.T = (self.P * self.V) / (self.n * self.R)
            return self.T
        elif param_to_find == 'n':
            self.n = (self.P * self.V) / (self.R * self.T)
            return self.n
        else:
            raise ValueError("Invalid parameter to find. Choose from 'P', 'V', 'T', or 'n'")

    def plot_isobar(self, P, V, T_range):
        # Sobrescribir el método de CharlesLaw para incluir n y R
        if self.n is None or self.R is None:
            raise ValueError("Both n and R must be defined for plotting isobar")
        volumes = [(self.n * self.R * T) / P for T in T_range]
        plt.plot(T_range, volumes)
        plt.xlabel('Temperature (K)')
        plt.ylabel('Volume (L)')
        plt.title('Isobar of Ideal Gas')
        plt.grid(True)
        plt.show()

    def plot_isotherm(self, P, V, pressure_range):
        if self.n is None or self.R is None or self.T is None:
            raise ValueError("Both n, R, and T must be defined for plotting isotherm")
        pressures = [(self.n * self.R * self.T) / V for V in self.calculate_volumes(P, V, pressure_range)]
        plt.plot(self.calculate_volumes(P, V, pressure_range), pressures)
        plt.xlabel('Volume (L)')
        plt.ylabel('Pressure (atm)')
        plt.title(f'Isotherm of Ideal Gas at T = {self.T} K')
        plt.grid(True)
        plt.show()
        
    def calculate_volumes(self, P, V, pressure_range):
        # Calcular los volúmenes para la isoterma basado en la gama de presiones proporcionada
        return [(self.n * self.R * self.T) / P for P in pressure_range]

class DaltonsLaw:
    
    def __init__(self, P_total=None, partial_pressures=None, masses=None, molar_masses=None, V=None, T=None, R=0.0821):
        self.P_total = P_total
        self.partial_pressures = partial_pressures  # Lista de presiones parciales
        self.masses = masses  # Lista de masas
        self.molar_masses = molar_masses  # Lista de masas molares
        self.V = V  # Volumen
        self.T = T  # Temperatura en Kelvin
        self.R = R  # Constante de gas ideal
    
    def calculate(self):
        if self.P_total is None and self.partial_pressures is not None:
            # Calcular la presión total a partir de las presiones parciales
            self.P_total = sum(self.partial_pressures)
            return self.P_total
        elif self.P_total is None and self.masses is not None and self.molar_masses is not None and self.V is not None and self.T is not None:
            # Calcular la presión total a partir de las masas, masas molares, volumen y temperatura
            self.partial_pressures = [(self.masses[i] / self.molar_masses[i]) * self.R * self.T / self.V for i in range(len(self.masses))]
            self.P_total = sum(self.partial_pressures)
            return self.P_total
        else:
            raise ValueError("Insufficient data to perform calculation.")