import math
import random

class player:
    def __init__(self, letter):
        #letter is x or o
        self.letter=letter

    #We want all players to get their next move
    def get_move(self, game):
        pass 

class RandomComputerPlayer(player):
    def __init__(self, letter):
        super().__init(letter)

    def get_move(self,game):
        pass

class HumanPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        pass



