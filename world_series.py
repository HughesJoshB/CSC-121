# Joshua Hughes
# GUI Porject
# May 2nd 2017
# World Series Winner GUI


import tkinter
import tkinter.messagebox
# create the window

# modify root window
##root.title("World Series Winners")
##root.geometry("300x300")

class WorldSeriesWinnersGUI:
    def __init__(self):
        # Create the Main Window
        self.main_window = tkinter.Tk()
	# Create two frames to group widgets
        self.top_frame = tkinter.Frame(self.main_window)
	
        self.bottom_frame = tkinter .Frame(self.main_window)
	# Create the widgets for the top frame
        self.prompt_label = tkinter.Label(self.top_frame, \
                                          text='What Year are you looking for the winner of?')
        self.year_entry = tkinter.Entry(self.top_frame, \
                                        width=10)
						
	#Pack the top frame's widgets
        self.prompt_label.pack(side='left')
        self.year_entry.pack(side='left')
        # Create a button widget for the bottom frame
        self.search_button = tkinter.Button(self.bottom_frame, \
                                            text='Search', \
                                            command=self.search)
        self.quit_button = tkinter.Button(self.bottom_frame, \
                                          text='Quit', \
                                          command=self.main_window.destroy)
        # Pack the Buttons
        self.search_button.pack(side='left')
        self.quit_button.pack(side='left')
        # Pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()
        # Enter the tkinter main loop
        tkinter.mainloop()
	
	# create the search def
    def search(self):
                                
        # Get the year and store as variable
        #year = int(self.year_entry.get())
        # open a file
        file_read = open('WorldSeriesWinners.txt', 'r')
        # read the file and close file
        team = file_read.readlines()
        file_read.close()
        
        # Intial file year
        year = 1903
        #create the dictionaries
        dctNum = {}
        dctYear = {}
               
        index = 0
        while index < len(team):
            ##tkinter.messagebox.showinfo(index)
            dctNum[year] = team[index].rstrip('\n')
            
            if year == 1904:
                dctNum[1904] = 'Not Played!'
            elif year == 1994:
                dctNum[1994] = 'Not Played!'
                                     
            else:
                
                dctNum[year] = team[index]
                
                
                   
            index += 1
            
            ##tkinter.messagebox.showinfo(index)
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

        year = int(self.year_entry.get())
        teamyear = dctNum.get(year)
        teamtimes = dctYear.get(teamyear)        

        tkinter.messagebox.showinfo('Winner', \
                                    str(teamyear)
                                    + ' was '+ str(year)) 
                                    ##'they have won a total of', + str(teamtimes), '.'))

# create an instance of the WorldSeriesWinnersGUI class
world_series = WorldSeriesWinnersGUI()
