# This program ask a user to pick a MLB team
# to see if they won a World Series and
# display the number of times won
# Feb 13th,  2017
# CSC-121 M2HW2 - World Series Champions
# Joshua Hughes



   # import the World Series text file


def main():

    #open the file
    infile = open('WorldSeriesWinners.txt', 'r')
    for line in open('WorldSeriesWinners.txt'):
        line = line.rstrip('\n')

    #Read the file
    Champion = infile.read().splitlines()

    # Close the file
    infile.close()

    # Ask user to enter a team name
    team = input('Please enter a team name:')
    ring = 0
    for Champion in Champion:
        if team == Champion:
            ring = ring+1
        
    # Display the total
    if ring == 1:
        print('The', team ,'did win' , ring, 'World Series')
    elif ring > 1:
        print('They', team, 'won a total of', ring, 'World Series')
    else:
        print('They suck and are losers!!!!!!!!')
        

# Call the main
main()

