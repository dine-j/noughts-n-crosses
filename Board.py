class Board:
    
    def __init__(self):
        self.matrix = [ [' ', ' ', ' '],
                       [' ', ' ', ' '],
                       [' ', ' ', ' '] ]
        self.last_move = (-1, -1)
        self.last_piece = ' '
        self.size = 3
        self.center = (1,1)
    
    def setSquare(self, piece, (x, y)):
        self.matrix[x][y] = piece
        self.last_move = (x, y)
        self.last_piece = piece
        
    def checkState(self):
        return self.checkWin() or self.checkDraw()
    
    def checkWin(self):
        win = True
        for col in range(self.size):
            if self.matrix[self.last_move[0]][col] != self.last_piece:
                win = False
        if win:
            return True
        
        for row in range(self.size):
            if self.matrix[row][self.last_move[1]] != self.last_piece:
                win = False
        if win:
            return True
        
        if self.last_move[0] == self.last_move[1]:
            for d in range(self.size):
                if self.matrix[d][d] != self.last_piece:
                    win = False
                    
        if self.checkDiagonal():
            return True
        
        return False
    
    def checkDraw(self):
        count = 0
        for x in range(self.size):
            for y in range(self.size):
                if self.matrix[x][y] != ' ':
                    count += 1
        return count == 9
    
    def checkDiagonal(self):
        win = True
        # top-left to bottom-right
        for d in range(self.size):
            if self.matrix[d][d] != self.last_piece:
                win = False
        
        if win:
            return True
        win = True
        
        # bottom-left to top-right
        x = self.size - 1
        y = 0
        while y < self.size:
            if self.matrix[x][y] != self.last_piece:
                win = False
            x -= 1
            y += 1
        
        if win:
            return True
        
        return False
    
    def isCorner(self, (x,y)):
        return (x,y) == (0,0) or (x,y) == (0, self.size - 1) or (x,y) == (self.size - 1, 0) or (x,y) == (self.size - 1, self.size - 1)
    
    def isEmpty(self, (x,y)):
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