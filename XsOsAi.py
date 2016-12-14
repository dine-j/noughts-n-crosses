from abc import ABCMeta, abstractmethod

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
        
   

class PerfectAi(Ai):
    
    def __init__(self, game, player_type):
        super(self, game, player_type)
    
        