
Dhiraj Totwani
Final Project: TicTacToe
README!

Contents:
gamescore.txt (I/O: Score Storage file)
Tic_Tac_Toe.py (Main Program)
Player.py (Player Class)

Description: The program is input based game called Tic-Tac-Toe.

The program is useful for those who like playing the game, but don't necessarily
want to draw a board and waste paper everytime they play against someone. The 
program/game also keeps track of the people's name and the amount of times they win 
before they decide to exit the program. The program validates the input and 
allows the user to see what they might have entered wrong. The program has a board
with 9 empty cells that can be filled with either X or O on a turn by turn basis. 
The input parameters are from 1-9. The boards empty spots are numbered. The numbers
are reference to the point that the user wants to fill with X or O.

The program checks if the player has won or if the game is tied after each turn. 
The user has the option to either continue playing or deciding to exit the program.
The exit function triggers the program to write the name, and score of the 2 players
into a "gamescore.txt" file. The content is appended to store as many sessions the players
decide to have. This keeps a directory of the scores of each session that can be looked 
at. This makes it easier for the players to reference who won the most!

The Tic_Tac_Toe file contains the entire application logic. The main part of the file is 
the Board class. That is what contains the methods to fill and empty the board. The methods 
also check if the player has won or if the game is tied. The player.py file contains
the player class and methods. The methods are for storing the player's name and score. The
methods also allow for displaying those elements. The player class elements are private. 

Instructions: 

1. Run only the Tic_Tac_Toe.py program in a console!
2. Enter Player 1's name
3. Enter Player 2's name
4. Player 1 enter your input 1-9:
5. Player 2 enter your input 1-9:
6. Play until game is won or tied.
7. Prompt will appear to play again?
8. Click y to play again, otherwise enter anything else to exit
9. Go to gamescore.txt file and review your win/loss record against player 1 and 2
 