import math
import unittest

from calculator import calculate


class TestCalculate(unittest.TestCase):
	def test_addition(self):
		self.assertEqual(calculate(2, "+", 3), 5)

	def test_subtraction(self):
		self.assertEqual(calculate(5, "-", 2), 3)

	def test_multiplication(self):
		self.assertEqual(calculate(4, "*", 3), 12)

	def test_square_root(self):
		self.assertEqual(calculate(9, "sqrt", 0), math.sqrt(9))

	def test_unsupported_operator(self):
		with self.assertRaisesRegex(ValueError, "Unsupported operator"):
			calculate(2, "/", 3)


if __name__ == "__main__":
	unittest.main()
