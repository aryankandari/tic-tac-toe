import math
import random

class Player:
    def __init__(self,letter):
        self.letter = letter    #O or X

    #get all players get next move given a game
    def get_move(self,game):
        pass

class RandomPCPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        square = random.choice(game.available_moves())
        return square

class UserPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8):')
            #check that this is the correct value by trying to cast it to integer and if not 
            #then we say invalid and if that spot is not available on the board then also invalid
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')

        return val
