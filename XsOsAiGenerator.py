from XsOsAi import RandomAi, PerfectAi

class AiGenerator:
    
    def __init__(self, level):
        if level == "random":
            self.ai = RandomAi()
        elif level == "perfect":
            self.ai = PerfectAi()