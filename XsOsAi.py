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
        super(RandomAi, self).__init__(game, player_type)
        
    def play(self):
        x = randint(0,2)
        y = randint(0,2)
        while not self.game.isEmpty((x, y)):
            x = randint(0,2)
            y = randint(0,2)
        self.game.setSquare(self.player_type, (x, y))

class PerfectAi(Ai):
    
    def __init__(self, game, player_type):
        super(PerfectAi, self).__init__(game, player_type)
        self.first_move = True
        
    def play(self):
        if self.win(): 
            print("win")
            return
        
        if self.blockOpponent(): 
            print("block")
            return
        
        if self.playCenter(): 
            print("playcenter")
            return
    
        if self.playOppositeCorner(): 
            print("playopposite")
            return
    
        if self.playCorner(): 
            print("playcorner")
            return
    
        self.playEmptySide()
    
    def win(self):
        empty = ' '
        count = 0
        (x,y) = (-1,-1)
        
        for col in range(self.game.size):
            square = self.game.matrix[self.game.last_move[0]][col]
            if square == self.player_type:
                count += 1
            if square == empty:
                (x,y) = (self.game.last_move[0],col)
        if count == 2 and (x,y) != (-1,-1):
            self.game.setSquare(self.player_type, (x,y))
            self.first_move = False
            return True
        
        count = 0
        (x,y) = (-1,-1)
        
        for row in range(self.game.size):
            square = self.game.matrix[row][self.game.last_move[1]]
            if square == self.player_type:
                count += 1
            if square == empty:
                (x,y) = (row,self.game.last_move[1])
        if count == 2 and (x,y) != (-1,-1):
            self.game.setSquare(self.player_type, (x,y))
            self.first_move = False
            return True
                
        count = 0
        (x,y) = (-1,-1)
        
        # top-left to bottom-right
        for d in range(self.game.size):
            square = self.game.matrix[d][d]
            if square == self.player_type:
                count += 1
            if square == empty:
                (x,y) = (d,d)
                    
        if count == 2 and (x,y) != (-1,-1):
            self.game.setSquare(self.player_type, (x,y))
            self.first_move = False
            return True
        
        count = 0
        (x,y) = (-1,-1)
        
        # bottom-left to top-right
        x = self.game.size - 1
        y = 0
        while y < self.game.size:
            square = self.game.matrix[x][y]
            if square == self.player_type:
                    count += 1
            if square == empty:
                    (x,y) = (d,d)
            x -= 1
            y += 1
        
        if count == 2 and (x,y) != (-1,-1):
            self.game.setSquare(self.player_type, (x,y))
            self.first_move = False
            return True

        return False
    
    def blockOpponent(self):
        empty = ' '
        count = 0
        (x,y) = (-1,-1)
        
        for row in range(self.game.size):
            for col in range(self.game.size):
                square = self.game.matrix[row][col]
                print square
                if square != empty and square != self.player_type:
                    count += 1
                if square == empty:
                    (x,y) = (row,col)
    
            print count
            if count == 2 and (x,y) != (-1,-1):
                self.game.setSquare(self.player_type, (x,y))
                self.first_move = False
                return True
            
            count = 0
            (x,y) = (-1,-1)
        
        for col in range(self.game.size):
            for row in range(self.game.size):
                square = self.game.matrix[row][col]
                if square != empty and square != self.player_type:
                    count += 1
                if square == empty:
                    (x,y) = (row,col)
                    
            if count == 2 and (x,y) != (-1,-1):
                self.game.setSquare(self.player_type, (x,y))
                self.first_move = False
                return True
        
            count = 0
            (x,y) = (-1,-1)
        
        # top-left to bottom-right
        for d in range(self.game.size):
            square = self.game.matrix[d][d]
            if square != empty and square != self.player_type:
                count += 1
            if square == empty:
                (x,y) = (d,d)
                    
        if count == 2 and (x,y) != (-1,-1):
            self.game.setSquare(self.player_type, (x,y))
            self.first_move = False
            return True
        
        count = 0
        (x,y) = (-1,-1)
        
        # bottom-left to top-right
        row = self.game.size - 1
        col = 0
        while col < self.game.size:
            square = self.game.matrix[row][col]
            if square != empty and square != self.player_type:
                count += 1
            if square == empty:
                (x,y) = (d,d)
            row -= 1
            col += 1
        
        if count == 2 and (x,y) != (-1,-1):
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
        if self.game.isCorner(self.game.last_move):
            if x != y:
                self.game.setSquare(self.player_type, (x,y))
            elif x == 0:
                self.game.setSquare(self.player_type, (self.game.size - 1,self.game.size - 1))
            else:
                self.game.setSquare(self.player_type, (0,0))
            return True
        return False
        
    def playCorner(self):
        corners = [(0,0), (0,self.game.size - 1), (self.game.size - 1, 0), (self.game.size - 1, self.game.size - 1,0)]
        
        for position in corners:
            if self.game.isEmpty((position[0], position[1])):
                self.game.setSquare(self.player_type, position)
                return True
        return False
    
    def playEmptySide(self):
        if self.game.isEmpty((0,1)):
            self.game.setSquare(self.player_type, (0,1))
        if self.game.isEmpty((1,0)):
            self.game.setSquare(self.player_type, (1,0))
        if self.game.isEmpty((2,1)):
            self.game.setSquare(self.player_type, (2,1))
        if self.game.isEmpty((1,2)):
            self.game.setSquare(self.player_type, (1,2))
        
        
        
    
        