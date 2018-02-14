# This program reads a file and averages the numbers and adds exceptions
# Jan 31 2017
# CTI-110 M1HW2 - Exception Handling
# Joshua Hughes


def main():
    try: 
        # Initialize an accumulator
        total = 0
        count = 0
        avg = 0

        # Open and read file named numbers.txt
        infile = open('numbers(1).txt', 'r')

        for line in infile:
            amount = float(line)
            total += amount
            count += 1
        
        #Close the file

        infile.close()

    
        # Avg the total numbers
        avg = amount / count

        print(format(avg, ',.2f'))

    except IOError:
        print('File not found')
       

    except ValueError:
        print('Please use numeric value instead of word')
        print(count+1)
        print(line)


main()
