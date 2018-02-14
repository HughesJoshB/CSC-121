def main():
    # Initialize an accumulator
    total = 0
    count = 0
    avg = 0
    line = 0

    # Open and read file named numbers.txt
    infile = open('numbers.txt', 'r')
    line = infile.readline()
    while line != '':
        amount = float(line)
        
        total += amount
        count += 1
        
    #Close the file

    infile.close()

    
    # Avg the total numbers
    avg = total / count

    print(format(avg, ',.2f'))


main()
