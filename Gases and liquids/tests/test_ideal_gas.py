import unittest
from ideal_gas import BoyleLaw
from ideal_gas import CharlesLaw
from ideal_gas import IdealGasLaw
from ideal_gas import DaltonsLaw

class TestBoyleLaw(unittest.TestCase):

    def setUp(self):
        self.boyle = BoyleLaw()

    def test_calculate_with_known_k_and_P1(self):
        self.boyle.k = 22.4
        self.boyle.P1 = 1
        V1 = self.boyle.calculate()
        self.assertAlmostEqual(V1, 22.4)

    def test_calculate_with_known_k_and_V1(self):
        self.boyle.k = 22.4
        self.boyle.V1 = 22.4
        P1 = self.boyle.calculate()
        self.assertAlmostEqual(P1, 1)

    def test_calculate_for_known_P1_V1_P2(self):
        self.boyle.P1, self.boyle.V1, self.boyle.P2 = 1, 22.4, 2
        V2 = self.boyle.calculate()
        self.assertAlmostEqual(V2, 11.2)

    def test_calculate_for_known_P1_V1_V2(self):
        self.boyle.P1, self.boyle.V1, self.boyle.V2 = 1, 22.4, 11.2
        P2 = self.boyle.calculate()
        self.assertAlmostEqual(P2, 2)

    def test_calculate_for_known_V1_P2_V2(self):
        self.boyle.V1, self.boyle.P2, self.boyle.V2 = 22.4, 2, 11.2
        P1 = self.boyle.calculate()
        self.assertAlmostEqual(P1, 1)

    def test_calculate_for_known_P1_P2_V2(self):
        self.boyle.P1, self.boyle.P2, self.boyle.V2 = 1, 2, 11.2
        V1 = self.boyle.calculate()
        self.assertAlmostEqual(V1, 22.4)

    def test_incorrect_parameters(self):
        with self.assertRaises(ValueError):
            self.boyle.calculate()

    def test_plot_isotherm(self):
        # This test ensures the plotting function runs without errors
        try:
            self.boyle.plot_isotherm(1, 22.4, range(1, 11))
            passed = True
        except Exception as e:
            passed = False
        self.assertTrue(passed)

    def test_plot_isotherm_from_k(self):
        # This test ensures the plotting function runs without errors
        try:
            self.boyle.plot_isotherm_from_k(22.4, range(1, 11), known='P')
            passed = True
        except Exception as e:
            passed = False
        self.assertTrue(passed)

class TestCharlesLaw(unittest.TestCase):

    def setUp(self):
        self.charles = CharlesLaw()

    def test_calculate_with_known_k_and_V1(self):
        self.charles.k = 22.4
        self.charles.V1 = 22.4
        T1 = self.charles.calculate()
        self.assertAlmostEqual(T1, 1)

    def test_calculate_with_known_k_and_T1(self):
        self.charles.k = 22.4
        self.charles.T1 = 1
        V1 = self.charles.calculate()
        self.assertAlmostEqual(V1, 22.4)

    def test_calculate_for_known_V1_T1_V2(self):
        self.charles.V1, self.charles.T1, self.charles.V2 = 22.4, 1, 44.8
        T2 = self.charles.calculate()
        self.assertAlmostEqual(T2, 2)

    def test_calculate_for_known_V1_T1_T2(self):
        self.charles.V1, self.charles.T1, self.charles.T2 = 22.4, 1, 2
        V2 = self.charles.calculate()
        self.assertAlmostEqual(V2, 44.8)

    def test_calculate_for_known_V2_T1_T2(self):
        self.charles.V2, self.charles.T1, self.charles.T2 = 44.8, 1, 2
        V1 = self.charles.calculate()
        self.assertAlmostEqual(V1, 22.4)

    def test_calculate_for_known_V1_V2_T2(self):
        self.charles.V1, self.charles.V2, self.charles.T2 = 22.4, 44.8, 2
        T1 = self.charles.calculate()
        self.assertAlmostEqual(T1, 1)

    def test_incorrect_parameters(self):
        with self.assertRaises(ValueError):
            self.charles.calculate()

    def test_plot_isobar(self):
        # This test ensures the plotting function runs without errors
        try:
            self.charles.plot_isobar(22.4, 1, range(1, 11))
            passed = True
        except Exception as e:
            passed = False
        self.assertTrue(passed)

    def test_plot_isobar_from_k(self):
        # This test ensures the plotting function runs without errors
        try:
            self.charles.plot_isobar_from_k(22.4, range(1, 11), known='V')
            passed = True
        except Exception as e:
            passed = False
        self.assertTrue(passed)

class TestIdealGasLaw(unittest.TestCase):

    def setUp(self):
        self.ideal_gas = IdealGasLaw()
        self.ideal_gas.R_unit = "L*atm/(mol*K)"
        self.ideal_gas.R = self.ideal_gas.get_R(self.ideal_gas.R_unit)
        self.ideal_gas.n = 1  # Asumiendo 1 mol de gas

    def test_get_R(self):
        self.assertEqual(self.ideal_gas.get_R("L*atm/(mol*K)"), 0.08205736608096)

    def test_calculate(self):
        self.ideal_gas.P, self.ideal_gas.V, self.ideal_gas.T = 1, 22.4, 273.15  # 1 atm, 22.4 L, 0°C en K
        self.assertAlmostEqual(self.ideal_gas.calculate('n'), 0.9993767482825312)  # Calculando moles de gas

        self.ideal_gas.n, self.ideal_gas.V, self.ideal_gas.T = 1, 22.4, 273.15
        self.assertAlmostEqual(self.ideal_gas.calculate('P'), 1.0006236404024207)  # Calculando presión en atm

        self.ideal_gas.P, self.ideal_gas.n, self.ideal_gas.T = 1, 1, 273.15
        self.assertAlmostEqual(self.ideal_gas.calculate('V'), 22.413969545014222)  # Calculando volumen en L

        self.ideal_gas.P, self.ideal_gas.V, self.ideal_gas.n = 1, 22.4, 1
        self.assertAlmostEqual(self.ideal_gas.calculate('T'), 272.9797587933734)  # Calculando temperatura en K

    def test_plot_isobar(self):
        # Esta prueba asegura que la función de trazar isobarra se ejecute sin errores
        try:
            self.ideal_gas.plot_isobar(1, 22.4, range(273, 373))  # Rango de temperatura de 0°C a 100°C
            passed = True
        except Exception as e:
            passed = False
        self.assertTrue(passed)

    def test_plot_isotherm(self):
        # Esta prueba asegura que la función de trazar isotermas se ejecute sin errores
        self.ideal_gas.T = 273.15  # Temperatura en K
        try:
            self.ideal_gas.plot_isotherm(1, 22.4, range(1, 11))  # Rango de presión de 1 atm a 10 atm
            passed = True
        except Exception as e:
            passed = False
        self.assertTrue(passed)

class TestDaltonsLaw(unittest.TestCase):

    def setUp(self):
        self.dalton = DaltonsLaw()

    def test_calculate_partial_pressures(self):
        self.dalton.masses = [28, 16, 32]
        self.dalton.molar_masses = [28.97, 32.00, 16.04]
        self.dalton.V = 1
        self.dalton.T = 300
        partial_pressures = self.dalton.calculate_partial_pressures()
        expected_pressures = [(28/28.97)*0.0821*300, (16/32.00)*0.0821*300, (32/16.04)*0.0821*300]
        for p, exp_p in zip(partial_pressures, expected_pressures):
            self.assertAlmostEqual(p, exp_p)

    def test_calculate_total_pressure_with_known_partial_pressures(self):
        self.dalton.partial_pressures = [1.0, 0.5, 0.8]
        P_total = self.dalton.calculate_total_pressure()
        self.assertAlmostEqual(P_total, 2.3)

    def test_calculate_total_pressure_with_known_masses_molar_masses_V_T(self):
        self.dalton.masses = [28, 16, 32]
        self.dalton.molar_masses = [28.97, 32.00, 16.04]
        self.dalton.V = 1
        self.dalton.T = 300
        P_total = self.dalton.calculate_total_pressure()
        self.assertAlmostEqual(P_total, sum([(28/28.97)*0.0821*300, (16/32.00)*0.0821*300, (32/16.04)*0.0821*300]))

    def test_incorrect_parameters(self):
        with self.assertRaises(ValueError):
            self.dalton.calculate_total_pressure()

# Run the tests
if __name__ == '__main__':
    unittest.main()