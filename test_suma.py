import unittest

from suma import sumar, restar, multiplicar, dividir

class TestSumar(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sumar(3, 2), 5)
        self.assertEqual(sumar(-1, 1), 0)
        self.assertEqual(sumar(-1, -1), -2)

    def test_resta(self):
        self.assertEqual(restar(5, 3), 2)
        self.assertEqual(restar(0, 5), -5)
        self.assertEqual(restar(-2, -2), 0)

    def test_multiplicacion(self):
        self.assertEqual(multiplicar(2, 3), 6)
        self.assertEqual(multiplicar(0, 5), 0)
        self.assertEqual(multiplicar(-2, 4), -8)

    def test_division(self):
        self.assertEqual(dividir(6, 3), 2.0)
        self.assertEqual(dividir(5, 2), 2.5)
        self.assertEqual(dividir(0, 5), 0)
        self.assertEqual(dividir(-8, 2), -4.0)


if __name__ == '__main__':
    unittest.main()