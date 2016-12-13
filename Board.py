class Board:
    
    def __init__(self):
        self.matrix = [ [' ', ' ', ' '],
                       [' ', ' ', ' '],
                       [' ', ' ', ' '] ]
    
    def setSquare(self, piece, (x, y)):
        self.matrix[x][y] = piece
        
    def __str__(self):
        string = ""
        for i in range(3):
            for j in range(3):
                if(self.matrix[i][j] == ' '):
                    string += "_ "
                else:
                    string += self.matrix[i][j] + " "
            string += "\n"
        return string