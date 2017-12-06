import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        calc = Calculator()
        result = calc.add(10, 10)
        self.assertEqual(result, 20)

    def test_multiplication(self):
        calc = Calculator()
        self.assertEqual(calc.mul(10, 10), 100)

if __name__ == "__main__":
    unittest.main()
