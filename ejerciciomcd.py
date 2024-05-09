import unittest

def mcd(a, b):
    """Calcula el máximo común divisor de dos números."""
    while b:
        a, b = b, a % b
    return a

def mcd_cuatro_numeros(a, b, c, d):
    """Calcula el máximo común divisor de cuatro números."""
    if 0 in [a, b, c, d]:
        raise ValueError("No se puede calcular el MCD si uno de los números es cero.")
    return mcd(mcd(a, b), mcd(c, d))



class TestCalculadora(unittest.TestCase):
    def test_mcd_cuatro_numeros_basico(self):
        # Pruebas básicas
        self.assertEqual(mcd_cuatro_numeros(10, 20, 30, 40), 10)
        self.assertEqual(mcd_cuatro_numeros(15, 30, 45, 60), 15)
        self.assertEqual(mcd_cuatro_numeros(17, 34, 51, 68), 17)

    def test_mcd_cuatro_numeros_primos(self):
        # Prueba con números primos
        self.assertEqual(mcd_cuatro_numeros(3, 5, 7, 11), 1)

    def test_mcd_cuatro_numeros_negativo(self):
        # Prueba con números negativos
        self.assertEqual(abs(mcd_cuatro_numeros(-10, -20, -30, -40)), 10)

    def test_mcd_cuatro_numeros_cero(self):
        # Prueba con un cero
        with self.assertRaises(ValueError):
            mcd_cuatro_numeros(0, 0, 30, 40)

    def test_mcd_cuatro_numeros_ceros(self):
        # Prueba con ceros
        with self.assertRaises(ValueError):
            mcd_cuatro_numeros(0, 0, 30, 40)
if __name__ == '__main__':
    unittest.main()
