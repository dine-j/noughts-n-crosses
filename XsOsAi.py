from abc import ABCMeta, abstractmethod
from random import randint

from Board import Board

class Ai:
    __metaclass__ = ABCMeta
    
    def __init__(self, game, player_type):
        self.game = game
        self.player_type = player_type
    
    @abstractmethod
    def play(self): pass


class RandomAi(Ai):
    
    def __init__(self, game, player_type):
        super(self, game, player_type)
        
    def play(self):
        x = randint(0,2)
        y = randint(0,2)
        while !self.game.checkEmptySquare((x, y)):
            x = randint(0,2)
            y = randint(0,2)
        self.game.setSquare(self.player_type, (x, y))

class PerfectAi(Ai):
    
    def __init__(self, game, player_type):
        super(self, game, player_type)
    
        