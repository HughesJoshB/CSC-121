# Joshua Hughes
# April 12th 2017
# Car class assignment
# M5HW2

increase = 5
decrease = 5
# create class Car
class Car:
	def __init__(self, year, make, speed):
		self.__year_model = year
		self.__make = make
		self.__speed = speed
	# Define the agrument for year_model
	def set_year(self, year):
		self.__year = year
	# define the agrument for make
	def set_make(self, make):
		self.__make = make
	# Define the agrument for speed
	def set_speed(self, speed):
		self.__speed = 0
	# Define the get agrument for year_model
	def get_year_model(self):
		return self.__year_model
	# Define the get agrument for make
	def get_make(self):
		return self.__make
	# Define the get agrument for speed
	def get_speed(self):
		return self.__speed
		
	# Define Accelerate
	def accelerate(self):
		self.__speed += increase
		
	# Define brake
	def brake(self):
		self.__speed -= decrease
		
