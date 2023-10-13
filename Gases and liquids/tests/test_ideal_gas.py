import unittest
from ideal_gas import BoyleLaw
from ideal_gas import CharlesLaw

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

# Run the tests
if __name__ == '__main__':
    unittest.main()

