# This program ask a user to enter a series of 20 numbers,
# store to a list, and then display the data
# Feb 9,  2017
# CSC-121 M2HW1 - Number Analysis
# Joshua Hughes



   # num_numbers is a constant
num_numbers = 20
   

def main():
    # Create a list to hold the numbers
    numbers = [0] * num_numbers
    total = 0
    index = 0
    NUM = 0
   
   

    while index < num_numbers :
        print('Enter a number ',index + 1,\
              ':', sep ='', end ='')
        NUM = int(input())
        numbers[index] = NUM
        index += 1
        total += NUM
        average = total/ num_numbers
        
    

    # Display the total
    print('The total of the numbers is', total)

    # Display the min number
    print('The lowest number was', min(numbers))

    # Display the highest number
    print('The highest number is', max(numbers))

    # Display the average
    print('The average for the numbers is', average)

# Call the main
main()
