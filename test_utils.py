import unittest

import utils


# Crear unha clase TestUtils que estenda de unittest.TestCase.
# Recoméndase usar nomes significativos para o nome da clase
class TestUtils(unittest.TestCase):
    def test_e_primo(self):
        self.assertFalse(utils.is_prime(4))
        self.assertTrue(utils.is_prime(2))
        self.assertTrue(utils.is_prime(3))
        self.assertFalse(utils.is_prime(8))
        self.assertFalse(utils.is_prime(10))
        self.assertTrue(utils.is_prime(7))
        self.assertEqual(
            utils.is_prime(-3), "Os números negativos non están permitidos"
        )

    def test_cube(self):
        self.assertEqual(utils.cubic(2), 8)
        self.assertEqual(utils.cubic(-2), -8)
        self.assertNotEqual(utils.cubic(2), 4)
        self.assertNotEqual(utils.cubic(-3), 27)

    def test_say_hello(self):
        self.assertEqual(utils.say_hello("Geekflare"), "Ola, Geekflare")
        self.assertEqual(utils.say_hello("Chandan"), "Ola, Chandan")
        self.assertEqual(utils.say_hello("Chandan"), "Ola, Chandan")
        self.assertEqual(utils.say_hello("Hafeez"), "Ola, Hafeez")


if __name__ == "__main__":
    unittest.main()
