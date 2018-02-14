# Joshua Hughes
# May 1st, 2017
# Sum of Numbers
# M7HW1

# This Program is to accept an integer and return the 
# sum of all the integers from 1 up to set integer

def main():
    num = 0
    # get input from user
    num = int(input('Enter a number greater than 1 to get a sum'\
        ' of numbers from 1 to your number. '))
    
    # return the sum value
    print('The sum of the integers from 1 to', num, 'is:', total(num))
	
def total(n):
    if n == 0:
        return n 
    else:
        return n + total(n-1)

# call the main
main()
