# Joshua Hughes
# M5HW3
# April 12, 2017
# Employee Class

import employee
def main():
    employees = make_list()
    print('Here is the employee files')
    print('Name\t\tId Number\tDepartment\tJob Title')
    print()
    display_list(employees)
	
	
def make_list():
    employee_list = []
	
    print('Enter the following Employee information.')
    for count in range(1,4):
        
                           
                
        # Get the employee name
        name = input('Enter employee name: ')
        idNumber = input('Enter employee ID: ')
        department = input('Enter employee department: ')
        jobTitle = input('Enter employee Job Tile: ')
        # create a object in memory and assign it to employee var
        emp = employee.Employee(name, idNumber, department, jobTitle)
        # Add object to list
        employee_list.append(emp)
    # return the list
    return employee_list


def display_list(employee_list):
    for employees in employee_list:
        print(employees.get_name(),'\t', employees.get_idNumber(),'\t\t',
             employees.get_department(),'\t', employees.get_jobTitle())
        
# Call the Main
main()
