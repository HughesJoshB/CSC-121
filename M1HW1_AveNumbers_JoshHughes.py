# This program reads a file and averages the numbers in file
# Jan 31 2017
# CSC-121 M1HW1 - Average Numbers
# Joshua Hughes


def main():
    # Initialize an accumulator
    total = 0
    count = 0
    avg = 0

    # Open and read file named numbers.txt
    infile = open('numbers.txt', 'r')

    for line in infile:
        amount = float(line)
        total += amount
        count += 1
        
    #Close the file

    infile.close()

    
    # Avg the total numbers
    avg = amount / count

    print(format(avg, ',.2f'))


main()
