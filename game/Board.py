class Board:
    def __init__(self):
        self.matrix = [[' ', ' ', ' '],
                       [' ', ' ', ' '],
                       [' ', ' ', ' ']]
        self.last_move = (-1, -1)
        self.last_piece = ' '
        self.size = 3
        self.center = (1, 1)

    def set_square(self, piece, (x, y)):
        self.matrix[x][y] = piece
        self.last_move = (x, y)
        self.last_piece = piece

    def check_state(self):
        return self.check_win() or self.check_draw()

    def check_win(self):
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

        if self.check_diagonal():
            return True

        return False

    def check_draw(self):
        count = 0
        for x in range(self.size):
            for y in range(self.size):
                if self.matrix[x][y] != ' ':
                    count += 1
        return count == 9

    def check_diagonal(self):
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

    def is_corner(self, (x, y)):
        return (x, y) == (0, 0) or (x, y) == (0, self.size - 1) \
               or (x, y) == (self.size - 1, 0) or (x, y) == (self.size - 1, self.size - 1)

    def is_empty(self, (x, y)):
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
