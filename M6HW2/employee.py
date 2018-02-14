# Joshua Hughes
# April 27th, 2016
# Employee/ProductionWorker/ShiftSupervisor Class
# M6HW2

class Employee():
      
    def __init__(self, name, idNumber):
        self.__name = name
        self.__idNumber = idNumber
    def set_name(self, name):
        self.__name = name
    def set_idNumber(self, idNumber):
        self.__idNumber = idNumber
    def get_name(self):
        return self.__name
    def get_idNumber(self):
        return self.__idNumber
		
class Worker(Employee):
    def __init__(self, name, idNumber, shiftNumber, payRate):
        # call superclass _init_ method
        Employee.__init__(self, name, idNumber)
        # create attributes for shiftNumber and payRate
        self.__shiftNumber = shiftNumber
        self.__payRate = payRate
    def set_shiftNumber(self, shiftNumber):
        self.__shiftNumber = shiftNumber
    def set_payRate(self, payRate):
        self.__payRate = payRate
    def get_shiftNumber(self):
        return self.__shiftNumber
    def get_payRate(self):
        return self.__payRate

class ShiftSupervisor(Employee):
    def __init__(self, name, idNumber, annualSalary, makeBonus, bonus):
        #call the superclass _init_ method
        Employee.__init__(name, idNumber)
        self.__annualSalary = annualSalary
        self.__makeBonus = makeBonus
        self.__bonus = bonus
    def set_annualSalary(self, annualSalary):
        self.__annualSalary = annualSalary
    def set_makeBonus(self, makeBonus):
        self.__makeBonus = makeBonus
    def set_bonus(self, bonus):
        self.__bonus
    def get_annualSalary(self):
        return self.__annualSalary
    def get_makeBonus(self):
        return self.__makeBonus
    def get_bonus(self):
        return self.__bonus
        
