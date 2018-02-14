# World Series Winners
# Joshua Hughes
# March 22nd , 2017
# 

def main():
        # open a file
        file_read = open('WorldSeriesWinners.txt', 'r')
        # read the file and close file
        team = file_read.readlines()
        file_read.close()
        
        ##teamName = team.rstrip()
        # Intial file year
        year = 1903
        #create the dictionaries
        dctNum = {}
        dctYear = {}

       
       

             
        index = 0
        while index < len(team):
                dctNum[year] = team[index].rstrip('\n')
                if year == 1904:
                        dctNum[1904] = 'There was no world series play that year!' 
                elif year == 1994:
                        dctNum[1994] = 'There was no world series play that year!' 
                        
                else:
                        dctNum[year] = team[index]
                
                index += 1
                year += 1

        for winner in team:
                total = 0
                index = 0
                while index < len(team):
                        if team[index] == winner:
                                total += 1
                        index += 1
                dctYear[winner] = total
        
       # print(dctNum)
       # print(dctYear)

        year= int(input('Enter a year for a World Series Winner: '))
        teamyear = dctNum.get(year)
        teamtimes = dctYear.get(teamyear)
        print('The team that won the world series in', year, 'was', teamyear, \
              'they have won a total of', teamtimes, '.')
main()
