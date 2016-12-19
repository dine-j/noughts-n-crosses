from XsOsAi import RandomAi, PerfectAi

class AiGenerator:
    
    def __init__(self, board, piece_type, level):
        if level == "random":
            self.ai = RandomAi(board, piece_type)
        elif level == "perfect":
            self.ai = PerfectAi(board, piece_type)
            
    def play(self):
        self.ai.play()