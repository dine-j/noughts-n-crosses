class Board:
    
    def __init__(self):
        self.matrix = [ [' ', ' ', ' '],
                       [' ', ' ', ' '],
                       [' ', ' ', ' '] ]
        self.last_move = (-1, -1)
        self.last_piece = ' '
    
    def setSquare(self, piece, (x, y)):
        self.matrix[x][y] = piece
        self.last_move = (x, y)
        self.last_piece = piece
        
    def checkState(self):
        for col in range(3):
            if self.matrix[last_move[0]][col] != last_piece:
                return false
        for row in range(3):
            if self.matrix[row][last_move[1]] != last_piece:
                return false
        if last_move[0] == last_move[1]:
            for d in range(3):
                if self.matrix[d] != last_piece:
                    return false
        return true
        
    def __str__(self):
        string = ""
        for i in range(3):
            for j in range(3):
                if self.matrix[i][j] == ' ':
                    string += "_ "
                else:
                    string += self.matrix[i][j] + " "
            string += "\n"
        return string