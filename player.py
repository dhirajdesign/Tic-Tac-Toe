# -*- coding: utf-8 -*-
"""
Tic-Tac-Toe
This file contains:
Player Class and Assert Unit Test

Includes private elements as player name and score that are stored in a 
dictionary. The dictionary is stored in a list object allowing it to hold the 
information of the 2 players playing the game.
"""

#import Tic_Tac_Toe as tic 

class player:
    """
    The player class is what stores the entire player information. This 
    module is imported into the Tic_Tac_Toe.py file. The methods in this
    are invoked to store player name and score.
    """
    #name and default score param of 0
    def __init__(self, name, score = 0):
        """
        This creates all the attributes of the player class. It creates a score
        name and profile object. The profile object is a dictionary that stores
        all the info of a single player. The dictionary is appended into the 
        profile_data list. The list then stores 2 instances of the profile obj
        for player 1 and player 2.
        """
        #create a private instance of name
        self.__name = name
        
        #create a private instance of score
        self.__score = score
        
        #create a private object/dictionary that holds both name and score
        self.__profile = {'name': self.__name, 'score':self.__score}
        
        #create a private list to store profile objects
        self.__profile_data = []
        
        #after each profile is created, append the new profile to the list
        self.__profile_data.append(self.__profile)
    
    
    def add_score(self, name):
        """
        This method matches the given name with the name in the dictionary
        that stores its score. This then adds 1 to that score every time it 
        is invoked. The method loops through the list element to find the 
        name of the person and add to his/her score.
        """
        
        #loop through the profile list
        for i in range(len(self.__profile_data)):
            
            #if the name parameter matches the name in the current dictionary
            if name == self.__profile_data[i]['name']:
                
                #add 1 to the score element in that dictionary
                self.__profile_data[i]['score'] += 1
    
    def get_profile(self, name):
        """
        This gets the profile of the player by using their name as a parameter.
        The name is given and matched with the dictionary object inside the 
        list. When there is a match it returns the 'name' and 'score' 
        dictionary object from that index value stored in the list. It is 
        formatted to return "Player has won 2 times!" Player is the player name
        and 1 is the score for example.
        """
        
        #loop through the length of the list of players
        for i in range(len(self.__profile_data)):
            
            #if the player's name matches the name attribute in the dictionary
            if name == self.__profile_data[i]['name']:
                
                #return and format the values in the dictionary, name and score
                return "\n" + str(self.__profile_data[i]['name']) \
            + " has won " + str(self.__profile_data[i]['score']) + " times!"
        
    def get_profile_data(self):
        """
        This returns all the dictionaries stored in the list. It formats it
        to return as "Player has won 2 times!" on every new line. This can be 
        further developed into a high score function by using it to compare
        with the other scores held. This function is not used in the program,
        but can be used to quickly print all the information in the list.
        """
        
        #loop through the len of the list
        for i in range(len(self.__profile_data)):
            
            #return the data stored in the list indice and format it with text
            return self.__profile_data[i]['name'] + "has won" + \
        self.__profile_data[i]['score'] + " times!" + "\n" 
            
    
    
#if __name__ =='__main__':
    
#Unit Testing for functions in the Player Class
#    player1 = player('Dhiraj')
#    assert player1.add_score('Dhiraj')
#    assert player1.get_profile('Dhiraj')
#    assert player1.get_profile_data
#    
#Unit Testing for functions in the Tic_Tac_Toe.py module
#   
#    X = 'X'
#    board = tic.Board()
#    assert board.display()
#    assert board.update_cells(1,"X")
#    assert board.get_cell(1)
#    assert board.is_winner("X")
#    assert board.is_tied()
#    assert board.is_exit(1)
#    assert board.new()
#    assert tic.print_header()
#    assert tic.refresh_screen()
#    
    
    

    
    
