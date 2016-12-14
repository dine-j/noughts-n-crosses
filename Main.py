from Board import Board
from XsOsAiGenerator import AiGenerator

def main():
    game = Board()
    
    player = ''
    player = raw_input("\nHi there, are you going to play x or o? ")
    
    difficulty = raw_input("\nEasy or hard? ")
    
    if difficulty == "easy":
        difficulty = "random"
    else:
        difficulty = "perfect"
        
    if player == 'x':
        ai = AiGenerator(game, 'o', difficulty)
    else:
        ai = AiGenerator(game, 'x', difficulty)
        ai.play()
        print game
        
    while True:
        player_move = (input("\nx? "), input("\ny? "))
        game.setSquare(player, player_move)
        ai.play()
        print game
        if game.checkState():
            break
        
    print("The end")
        
    
    
if __name__ == "__main__": main()