# importar o módulo unittest
import unittest

from utils import is_prime


# Crear unha clase TestUtils que estenda de unittest.TestCase.
# Recoméndase usar nomes significativos para o nome da clase
class TestUtils(unittest.TestCase):
    def test_is_prime(self):
        self.assertFalse(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(7))

    def test_non_prime_number(self):
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(10))

    def test_negative_number(self):
        self.assertEqual(is_prime(-3), "Os números negativos non están permitidos")


if __name__ == "__main__":
    unittest.main()
