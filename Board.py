class Board:
    
    def __init__(self):
        self.matrix = [ [' ', ' ', ' '],
                       [' ', ' ', ' '],
                       [' ', ' ', ' '] ]
        self.last_move = (-1, -1)
        self.last_piece = ' '
        self.size = 3
    
    def setSquare(self, piece, (x, y)):
        self.matrix[x][y] = piece
        self.last_move = (x, y)
        self.last_piece = piece
        
    def checkState(self):
        for col in range(self.size):
            if self.matrix[self.last_move[0]][col] != self.last_piece:
                return False
        for row in range(self.size):
            if self.matrix[row][self.last_move[1]] != self.last_piece:
                return False
        if self.last_move[0] == self.last_move[1]:
            for d in range(self.size):
                if self.matrix[d][d] != self.last_piece:
                    return False
        return True
    
    def checkEmptySquare(self, (x, y)):
        return self.matrix[x][y] == ' '
        
    def __str__(self):
        string = ""
        for i in range(self.size):
            for j in range(self.size):
                if self.matrix[i][j] == ' ':
                    string += "_ "
                else:
                    string += self.matrix[i][j] + " "
            string += "\n"
        return string