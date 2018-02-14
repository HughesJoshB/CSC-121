# Joshua Hughes
# April 26th 2017
# Employee and Production Worker Class
# M6HW1

import employee

def main():
      
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

# call the main	
main()
	
	
