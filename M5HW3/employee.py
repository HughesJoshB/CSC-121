# Joshua Hughes
# M5HW3
# April 12, 2017
# Employee Class

# define the class
class Employee:
	def __init__(self, name, idNumber, department, jobTitle):
		self.__name = name
		self.__idNumber = idNumber
		self.__department = department
		self.__jobTitle = jobTitle
	
	def set_name(self, name):
		self.__name = name
	
	def set_idNumber(self, idNumber):
		self.__idNumber = idNumber
	
	def set_department(self, department):
		self.__department = department
	
	def set_jobTitle(self, jobTitle):
		self.__jobTitle = jobTitle
	
	def get_name(self):
		return self.__name
	
	def get_idNumber(self):
		return self.__idNumber
	
	def get_department(self):
		return self.__department
	
	def get_jobTitle(self):
		return self.__jobTitle
