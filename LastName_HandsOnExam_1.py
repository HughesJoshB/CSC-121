# Joshua Hughes
# March 23, 2017
# Hands on in Class Exam
'''
Hands On Exam #1

U will be presented with a menuu
First thing is to make sure the program will run
I have given you the basic structure so do NOT alter the basic structure

Based on the menu we will choose 1 then 2 then 3 in that order

1)If an user chooses 1 then you will need to create a text file called LastName_Test.txt
  The contents of the file should be your name only. Do not display. However I would make sure it works
  Give the user a message the name was written to the file LastName_Test.txt
2)If an user chooses 2 then you will need to display the contents of the file named LastName_Test to the desktop
  The contents of the file should be your name only
  Make sure you check to see if the file exists if not give an appropriate error message
3)If an user chooses 3 then you will need to create an empty list and get user input to add these numbers to the list:
  Add 10,20,30,40 to the list and then add them up with a for loop
  Then display the numbers and the total with an appropiate message
Make sure to check to see if the user wants to run the program
'''
print()
print("Hands On Test #1 Menu")
print()
print("Make a Selection")
print()
print("1. Create a Text File")
print("2. Display Contents of Text File")
print("3. Create and Display a List")
print()
choice = "y"


while choice != "n":
    num = int(input("Enter a menu choice: "))
    if num == 1:
        # print(num)
        print('Enter your name: ')
        name = input()
        # open a file named LastName_Test.txt
        userName = open('LastName_Test.txt', 'w')
        # write the name to a file
        userName.write(name)
        # close the file
        userName.close()
        print('Your name has be written to LastName_Test.txt.')
    elif num == 2:
        # print(num)
        try:
            
            # open the file LastName_Test
            infile = open('LastName_Test.txt', 'r')
            # Read the File
            lastName = infile.read()
            # close the file
            infile.close()
            # Display the name in the file
            print('The data in the file is : ', lastName)
        # Create Error Handler
        except IOError:

            print('That file is not found.')
            print('The file you are looking for is LastName_Test.txt')
        
        
    else:
            



            # Ceate a empty list
            num_list = []
            total = 0
            # Create a variable to control the loop.
            again = 'y'
            # Add some numbers to the list.
            while again == 'y':
                # Get the numbers from the user
                num = int(input('Enter a number: '))
                # Append the list
                num_list.append(num)
                # Add another number
                print('Do you want to add another number?')
                again = input('y = yes, anything else = no: ')
                print()
            # Display the number in the list.
            print('The numbers that you entered are: ')

            for num in num_list:
                   print(num)
                   
           
        # Calculate the total of the list elements
            for num in num_list:
                total += num
            
            print('The total of the number is: ', total)
            
        

            
    choice = input("Run the program again (y/n)?: ")
    print()
    
print('Good job')
print()
