#!/usr/bin/pyhon2.7.9

import unittest
import mock
import math

from calc import calc
from exception import *

class calc_test(unittest.TestCase):
	def setUp(self):
		self.calc = calc()
	
	def test_adding_two_string(self):
		self.assertRaises(notANumber, self.calc.add, "str1", "str2")
	
	def test_division_by_zero(self):
		self.assertRaises(divByZero, self.calc.divide, 4, 0)
	
	def test_log_from_negative(self):
		self.assertRaises(isNegative, self.calc.ln, -4)
	
	def test_derivative_with_no_function(self):
		self.assertRaises(notFunction, self.calc.der, 4, 6, 1)
	
	@mock.patch("calc.calc.der", return_value = 1)
	def test_derivative_(self, mock_value):
		func = math.cos
		x = 0
		prec = 0.1
		expected = 1
		self.assertEqual(calc.der(func, x, prec), expected)
		
	def test_adding_float_to_int(self):
		x = 4.3
		y = 3
		exp = 7.3
		self.assertEqual(self.calc.add(x, y), exp)

if __name__ == "__main__":
	unittest.main()
