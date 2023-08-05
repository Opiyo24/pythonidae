import math
import random

class Player:
    def __init__(self, letter):
        #letter is x or o
        self.letter = letter

     #we want all players to get their next move given a game
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player): #Using inheritence
    def __init__(self, letter):
        super().__init__(letter) #Using supper class


    def get_move(self, game):
        #Get a random valid spot for our next move
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-9):')
            #We are going to check that this is a correct value by trying to cats
            #it to an integer, amd if its is not, then we say ity's invalid
            # if that spot is not available on the board, we also say its invalid
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True # If these are successful, then yay!
            except ValueError:
                print("Invalid square. Try again.")
        
        return val