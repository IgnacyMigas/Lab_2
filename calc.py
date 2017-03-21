#!/usr/bin/pyhon2.7.9

import abc
from math import log
from scipy.misc import derivative
from exception import *

class abstractCalc(object):
	__metaclass__ = abc.ABCMeta
	@abc.abstractmethod
	def add(delf, x, y):
		pass
	
	@abc.abstractmethod
	def divide(delf, x, y):
		pass
	
	@abc.abstractmethod
	def ln(delf, x):
		pass
	
	@abc.abstractmethod
	def der(delf, x, y):
		pass

class calc(abstractCalc):
	def add(self, x, y):
		self.isANumber(x)
		self.isANumber(y)
		return x+y
	
	def divide(self, x, y):
		self.isANumber(x)
		self.isANumber(y)
		self.isAZero(y)
		return x/y
	
	def ln(self, x):
		self.isANumber(x)
		self.isAZero(x)
		self.isANegative(x)
		return log(x)
	
	def der(self, func, x, prec):
		self.isANumber(x)
		self.isAZero(prec)
		self.isANegative(prec)
		self.isAFunction(func)
		return derivative(func, x, prec)
	
	def isANumber(self, x):
		if not isinstance(x, (int, float)):
			raise notANumber()
	
	def isAZero(self, x):
		if x == 0:
			raise divByZero()
	
	def isANegative(self, x):
		if x < 0:
			raise isNegative()
	
	def isAFunction(self, func):
		if not callable(func):
			raise notFunction()
