# tests/test_discount.py
import unittest
from discount import calculate_discount

class TestDiscount(unittest.TestCase):

    def test_discount_applied(self):
        self.assertEqual(calculate_discount(100, 25), 75)

    def test_discount_not_applied(self):
        self.assertEqual(calculate_discount(100, 10), 100)

    def test_zero_discount(self):
        self.assertEqual(calculate_discount(100, 0), 100)

    def test_negative_values(self):
        with self.assertRaises(ValueError):
            calculate_discount(-100, 25)
        with self.assertRaises(ValueError):
            calculate_discount(100, -25)

if __name__ == "__main__":
    unittest.main()
