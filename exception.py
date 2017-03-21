#!/usr/bin/pyhon2.7.9

class notFunction(Exception):
	def __str__(self):
		return repr("Argument 1 is not a function")

class divByZero(Exception):
	def __str__(self):
		return repr("Division by zero")

class notANumber(Exception):
	def __str__(self):
		return repr("Argument is not float or int")

class isNegative(Exception):
	def __str__(self):
		return repr("Argument is negative number")
