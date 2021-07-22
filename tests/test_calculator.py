from unittest import TestCase
from src.calculator import Calculator


class TestCalculatorFunc(TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_sum_two_integer_numbers(self):
        result = self.calc.soma(2, 2)
        self.assertEqual(result, 4), f"{4} != {result}"
