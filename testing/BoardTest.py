from Board import Board

def main():
    game = Board()
    
    game.matrix = [ ['x', ' ', ' '],
                       [' ', 'x', ' '],
                       [' ', ' ', 'x'] ]
    game.last_piece = 'x'
    game.last_move = (0,0)
    assert(game.checkState() == True)
    
    game.last_move = (1,1)
    assert(game.checkState() == True)
    
    game.last_move = (2,2)
    assert(game.checkState() == True)
    
    
    game.matrix = [ ['o', ' ', ' '],
                       [' ', 'o', ' '],
                       [' ', ' ', 'o'] ]
    game.last_piece = 'o'
    game.last_move = (0,0)
    assert(game.checkState() == True)
    
    game.last_move = (1,1)
    assert(game.checkState() == True)
    
    game.last_move = (2,2)
    assert(game.checkState() == True)
    
    
    game.matrix = [ [' ', ' ', 'x'],
                       [' ', 'x', ' '],
                       ['x', ' ', ' '] ]
    game.last_piece = 'x'
    game.last_move = (2,0)
    assert(game.checkState() == True)
    
    game.last_move = (1,1)
    assert(game.checkState() == True)
    
    game.last_move = (0,2)
    assert(game.checkState() == True)
    
    
    game.matrix = [ [' ', ' ', 'o'],
                       [' ', 'o', ' '],
                       ['o', ' ', ' '] ]
    game.last_piece = 'x'
    game.last_move = (2,0)
    assert(game.checkState() == True)
    
    game.last_move = (1,1)
    assert(game.checkState() == True)
    
    game.last_move = (0,2)
    assert(game.checkState() == True)
    
    
if __name__ == "__main__": main()