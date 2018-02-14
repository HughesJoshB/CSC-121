# Joshua Hughes
# April 27th, 2017
# Employee/Production/ShiftSupervisor
# M6HW2

import employee

def main():
    print('Is the employee information for a regular employee' \
          'or Shift Supervisor? ')
    employeeInfo = int(input('Enter 1 for Regular Employee or 2 for Supervisor: '))
    if employeeInfo == 1:
        #define variables
        employeeName = ""
        employeeID = ""
        workShift = 0
        payPer = 0.0
	
        # Get infromation from user
        employeeName = input('Enter employees Name: ')
        employeeID = input('Enter employees ID Number: ')
        workShift = float(input('Which shift is employee working: '))
        payPer = float(input('Enter employees hourly pay rate: '))
	
        # create a object for workerInfo
        worker = employee.Worker(employeeName, employeeID, workShift, payPer)
        #display all information that has been store
        print('Here is the information on your Production Worker')
        print('Name: ', employeeName)
        print('ID Number: ', employeeID)
        print('Shift: ', workShift)
        print('Their Hourly Rate of Pay: ', payPer)

    elif employeeInfo == 2:
        #define variables
        employeeName = ""
        employeeID = ""
        annualSalary = ""
        makeBonus = ""
        bonus = 1000.00
        salary = 0.0
	
	# Get Information from user
        employeeName = input('Enter employees name: ')
        employeeID = input('Enter employee ID number: ')
        annualSalary = float(input('What is their annual salary: '))
        makeBonus = input('Did the supervisors department make annual production levels? yes or no: ')
        if makeBonus == 'yes':
            
            print('Their bonus will be: ', bonus)
            salary = annualSalary + bonus
            print('Their total salary for this year is: ', format(salary,'.2f'))
        else:
            print('They will not recieve a bonus this year')	
        # create a object for ShiftSupervisor
        shiftSupervisor = employee.ShiftSupervisor(employeeName, employeeID, annualSalary, makeBonus, bonus)
        print('--------------------')
        print('Here is the information for the Shift Supervisor.')
        print('Name: ', employeeName)
        print('ID Number: ', employeeID)
        print('Their Annual Salary for this year is: ', salary)
            
    else:
        print('Please enter a number of 1 or 2.')
		
		
        

# call the main	
main()
