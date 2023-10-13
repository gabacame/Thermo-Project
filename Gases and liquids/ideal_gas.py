import matplotlib.pyplot as plt
import numpy as np

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