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
        self.first_move = True
        
    def play(self):
        if self.win(): return
        
        if self.blockOpponent(): return
        
        if self.playCenter(): return
    
        if self.playOppositeCorner(): return
    
        if self.playCorner(): return
    
        if self.playEmptySide(): return
    
    def win(self):
        (x,y) = self.checkWin()
        if (x,y) != (-1,-1):
            self.game.setSquare(self.player_type, (x,y))
            self.first_move = False
            return True
        return False
    
    def blockOpponent(self):
        (x,y) = self.blockOpponent()
        if (x,y) != (-1,-1):
            self.game.setSquare(self.player_type, (x,y))
            self.first_move = False
            return True
        return False
    
    def playCenter(self):
        if self.player_type == 'x' and self.first_move:
            self.game.setSquare(self.player_type, self.game.center)
            self.first_move = False
            return True
        return False
    
    def playOppositeCorner(self):
        (y,x) = self.game.last_move
        if self.game.isCorner((y,x)):
            self.game.setSquare((x,y))
            return True
        return False
        
    def playCorner(self):
        corners = [(0,0), (0,self.game.size - 1), (self.game.size - 1, 0), (self.game.size - 1, self.game.size - 1,0)]
        
        for position in corners:
            if self.game.checkEmptySquare((x,y)):
                self.game.setSquare(self.player_type, (x,y))
                return True
        return False
        
        
    
        