# -*- coding: utf-8 -*-
"""
Dhiraj Totwani
Final Project
TIC-TAC-TOE

Description:
The game is a two player game. The 2 players will be assigned one output (X 
or O). They will be prompted to enter their name. Their name will be stored for
the purpose of keeping track of score if they decide to play against each other
multiple times. The input that they will be prompted to enter is from 1-9. The 
board's empty spots are numbered from left to right.The number represents where
the player elects to play their turn. 

EX. Board Layout   |                      Player Input
                   |
     1 | 2 | 3     |  Player_X enters 1 ->  X |   |  
    -----------    |                       -----------
     4 | 5 | 6     |                          |   |  
    -----------    |                       -----------   
     7 | 8 | 9     |                          |   | 0  <- Player_0 enters 9
                   |     
     
"""
import player as p #Player module used for the player class and methods
import os
os.system("cls")
    
class Board(): 
    """
    The Board class stores all the methods for creating the board and 
    maintaining the state of the board. 
    """
    def __init__(self):
        """
        This creates the list element that will fill itself when the player
        chooses an option to fill a specific cell of the board
        """
        #the cell list's indices will serve as the playable spots for the board
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    
    def display(self):
        
        """
        This method prints the board onto the console. This is what makes the
        game visible and sensible to the player. It assigns the list indices
        to the specific boxs that can be filled by the player with X/0>
        """
        
        #print/format the tictactoe board & add the list indices to the spots
        print (" %s | %s | %s " %(self.cells[1], self.cells[2], self.cells[3]))
        print ("-----------")
        print (" %s | %s | %s " %(self.cells[4], self.cells[5], self.cells[6]))
        print ("-----------")
        print (" %s | %s | %s " %(self.cells[7], self.cells[8], self.cells[9]))
        
    def update_cells(self, cell_no, player):
        
        """
        This updates the cell with X or O depending on the player that is 
        making the move. It doesn't edit a space that is already occupied.
        """
        
        #if the cell is empty
        if self.cells[cell_no] == " ": 
            
            #the cell will be filled with X or 0
            self.cells[cell_no] = player 
     
        #otherwise    
        else:
            
            #return False if the spot is not empty
            return False 
    
    def get_cell(self, cell_no):
        
        """
        this is a getter the gets the specific cell's content if invoked
        """
        
        #return the value stored in the cells list index
        return self.cells[cell_no] 
    
    def is_winner(self, player):
        
        """
        This determines the winner of the game. It checks for the 8 different
        combinations that a player would need to win. This function is then
        applied to check for winner in both instances of player X or player 0.
        """
        
        #if the cells(1,2,3) have the same player character 
        if self.cells[1]==player and self.cells[2] == player and self.cells[3]\
        == player: 
            return True
        
        #if the cells(4,5,6) have the same player character
        if self.cells[4]==player and self.cells[5] == player and self.cells[6]\
        == player: 
            return True
        
        #if the cells(7,8,9) have the same player character return true
        if self.cells[7]==player and self.cells[8] == player and self.cells[9]\
        == player:
            return True
        
        #if the cells(1,5,9) have the same player character return true
        if self.cells[1]==player and self.cells[5] == player and self.cells[9]\
        == player: 
            return True
        
        #if the cells(3,5,7) have the same player character return true
        if self.cells[3]==player and self.cells[5] == player and self.cells[7]\
        == player: 
            return True
        
        #if the cells(1,4,7) have the same player character return true
        if self.cells[1]==player and self.cells[4] == player and self.cells[7]\
        == player: 
            return True
        
        #if the cells(2,5,8) have the same player character return true
        if self.cells[2]==player and self.cells[5] == player and self.cells[8]\
        == player: 
            return True
        
        #if the cells(3,6,9) have the same player character return true
        if self.cells[3]==player and self.cells[6] == player and self.cells[9]\
        == player: 
            return True 
        
        #if they don't have a match return False
        return False 
    
    def is_tied(self):
        
        """
        This checks if the game is tied. If the game is tied then it returns
        true. It loops through the cells to see if there is any empty spots. 
        This function then identifies if all spots are filled by counting. If 
        all the spots are full it returns True. This function should only be 
        used after checking for the winner("is_winner()"), otherwise it has 
        a chance of giving a false positive.
        """
        
        #counter variable 
        used_spots = 0 
        
        #for loop to iterate over the list
        for cell in self.cells:  
            
            #if the list value is not an empty space
            if cell != " ": 
                
                #add to the counter
                used_spots += 1 
                
                #if the counter reaches 9
                if used_spots == 9:  
                    
                    #the game is a tie, return True
                    return True 
                
    def is_exit(self, no):
        
        """
        A function used for exiting the while loop in the main program.
        1 is used as the catalyst for the no parameter. If you want it to 
        return true then use 1 as the parameter for no. Otherwise use any
        other character to return false and use it to exit out of the while 
        loop that I used in the beginning of the program.
        """
        
        #if the condition is not 1 return false
        if no != 1: 
            return False
        
        #otherwise
        else:
            
            #if it is 1 then return true
            return True 
        
    def new(self):
        
        """
        This is used to clear the board and start a new game from scratch. 
        """
        
        #fill the list with empty spaces
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
        
    

def print_header():
    """
    This is used to print a header for the main program
    """
    
    #Print and introduce the game as header
    print("Welcome to Tic-Tac-Toe\n") 
    
def refresh_screen():
    """
    This clears the screen so that the program doesn't print multiple instances
    of the board every time a player plays in a spot. This function is called
    after the input of the player is received. 
    """
    #clear the old state of the board
    os.system("cls") 
    
    #print the header
    print_header() 
    
    #display the current state of the board
    board.display()
    
if __name__ == '__main__':
     
    
    #Initiate the board class 
    board = Board() 
        
    
    #Get player 1's name
    player_1 = input('1st Player enter your name: ') 
    
    #store it in the player class init method
    p_data1 = p.player(player_1) 
    
    #Get player 2's name
    player_2 = input('2nd Player enter your name: ') 
    
    #store name by calling the player class init
    p_data2 = p.player(player_2) 
    
    #empty variable that will store the player name of the winner
    winner = "" 
        
    #begin while loop, board.is_exit(1) == True
    while board.is_exit(1): 
        
        #refresh the screen and print the fresh board and head
        refresh_screen() 
    
    
        #true or false variable
        x = 0 
        
        #until x's value doesn't change, keep looping
        while x == 0: 
            try: 
                #try getting the integer input from the player 1
                x_choice = int(input("\n" + str(player_1) +" please choose" 
                                     " an input between 1 - 9 : "))
               
                #if the integer is between 1-9    
                if x_choice > 0 and x_choice < 10:
                    
                    #check the cell to see if it is empty/playable
                    if board.get_cell(x_choice) == " ":
                        
                        #update the cell with the string 'X'
                        board.update_cells(x_choice, "X")
                        
                        #change x to 1 from 0 and that should end the loop
                        x = 1
                        
                        #refresh the board to display the change
                        refresh_screen()
                        
                    else:
                        
                        #if the spot is filled then return it is filled
                        print('That spot is filled!')
                else:
                    
                    #if the numbers are larger or lower than 1-9 then prompt
                    print('Enter integers between 1-9 please!')
            except:
                
                #if the number is not an integer then print enter integers only
                print("Please enter integers only!")
                
                #continue the loop
                continue 
    
        
        #check if player 1 is winner
        if board.is_winner("X"): 
            
            #if winner then print player 1 wins
            print ("\n",player_1,"wins!\n") 
            
            #use the add_score method to save score
            p_data1.add_score(player_1) 
            
            #assign player 1 as the winner
            winner = player_1 
            
            #ask players if they want to play again
            play_again = input("Would you like to play again? (Press Y if yes "
                                        "or press any other key to exit)): " )
                    
            #if they respond y as in yes
            if play_again == "Y" or play_again == "y":
                
                #clear the board
                board.new() 
                
                #restart the loop
                continue 
            
            else: 
                
                #else print the number of wins each player won
                print(p_data1.get_profile(player_1), \
                      p_data2.get_profile(player_2))
                
                #end the loop, exit out of the program loop
                board.is_exit(0) 
                break
            
        #Check if the players are tied    
        elif board.is_tied():
            
            #if they are then return tie game
            print('Game is Tied!')
            
            #ask the players if they want to play again?
            play_again = input("Would you like to play again? (Press Y if yes "
                               "or press any other key to exit)): " )
                    
            #if they do then clear the board and start again
            if play_again == "Y" or play_again == "y":
                board.new()
                continue
            
            #else exit out of the program loop
            else:
                board.is_exit(0)
                break
        
        #a true or false variable
        o = 0 
        
        #until o is zero keep looping
        while o == 0: 
            
            try:
                
                #ask player 2 to enter an input between 1-9
                o_choice = int(input("\n" + str(player_2) + " please choose" 
                                     " an input between 1 - 9 : "))
                
                #if the integer is between 1-9  
                if o_choice > 0 and o_choice < 10:
                    
                    #check the cell to see if it is empty/playable
                    if board.get_cell(o_choice) == " ":
                        
                        #update the cell with the string '0'
                        board.update_cells(o_choice, "0")
                        
                        #change o to 1 from 0 and that should end the loop
                        o = 1
                        
                        #refresh the board to display the change
                        refresh_screen()
                        
                    else:
                        
                        #if the spot is filled then return it is filled
                        print('That spot is filled!')
                        
                else:
                    
                    #if the numbers are larger or lower than 1-9 then prompt
                    print('Enter integers between 1-9 please!')
                    continue
                
            except:
                
                #if the number is not an integer then print enter integers only
                print("Enter integers only")
                continue
            
            
        #check if player 2 is winner
        if board.is_winner("0"):
            
            #if winner then print player 2 wins
            print ("\n",player_2, "wins!\n")
            
            #use the add_score method to save score
            p_data2.add_score(player_2)
 
            #assign player 2 as the winner
            winner = player_2
            
            #ask players if they want to play again
            play_again = input("Would you like to play again? (Press Y if yes "
                               "or press any other key to exit)): " )
                    
            #if they respond y as in yes        
            if play_again == "Y" or play_again == "y":
                
                #clear the board
                board.new()
                
                #restart the loop
                continue
            
            else:
                
                #else print the number of wins each player won
                print(p_data1.get_profile(player_1), \
                      p_data2.get_profile(player_2))
                
                #exit the main program loop
                board.is_exit(0)
                break
            
        #Check if the players are tied    
        elif board.is_tied():
            
            #if they are then return tie game
            print('Game is Tied!')
            
            #ask if they want to play again
            play_again = input("Would you like to play again? (Press Y if yes "
                               "or press any other key to exit)): " )
                    
            #if they respond Y for yes 
            if play_again == "Y" or play_again == "y":
                
                #print a fresh board for the new game
                board.new()
                continue
            
            #otherwise
            else:
                
                #exit the main while loop and end the program
                board.is_exit(0)
                break
    
    #file name that will store game information
    filename =  'gamescore.txt'
    
    #if the file exist
    if os.path.exists(filename):
        
        #append if already exists
        append_write = 'a' 
        
        #open the file
        scores = open(filename,append_write)
        
        #Write the scores data into the file use the player class method
        scores.write("Game Scores: " +p_data1.get_profile(player_1) + '\n' + \
                     p_data2.get_profile(player_2) + '\n' + '----------------')
        
        #Close the file
        scores.close() 
        
    else: 
        
        #create a new file if it does not exist
        append_write = 'w' 
        
        #open the file
        scores = open(filename,append_write)
        
        #Write the scores data into the file use the player class method
        scores.write("Game Scores: " +p_data1.get_profile(player_1) + '\n' + \
                     p_data2.get_profile(player_2) + '\n' + '--------------' \
                     + '\n')
        
        #Close the file
        scores.close() 
            
            
    
        
    
        
            
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    