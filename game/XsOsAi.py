from abc import ABCMeta, abstractmethod
from random import randint


class Ai:
    __metaclass__ = ABCMeta

    def __init__(self, game, player_type):
        self.game = game
        self.player_type = player_type

    @abstractmethod
    def play(self): pass


class RandomAi(Ai):
    def __init__(self, game, player_type):
        super(RandomAi, self).__init__(game, player_type)

    def play(self):
        x = randint(0, 2)
        y = randint(0, 2)
        while not self.game.isEmpty((x, y)):
            x = randint(0, 2)
            y = randint(0, 2)
        self.game.setSquare(self.player_type, (x, y))


class PerfectAi(Ai):
    def __init__(self, game, player_type):
        super(PerfectAi, self).__init__(game, player_type)
        self.first_move = True

    def play(self):
        if self.fill_third_space():
            print("fill third space")
            return
        # if self.win():
        #     print("win")
        #     return
        #
        # if self.block_opponent():
        #     print("block")
        #     return

        if self.play_center():
            print("playcenter")
            return

        if self.play_opposite_corner():
            print("playopposite")
            return

        if self.play_corner():
            print("playcorner")
            return

        self.play_empty_side()

    def fill_third_space(self):
        empty = ' '
        win_count = 0
        block_count = 0
        blocks = []
        (x, y) = (-1, -1)

        for row in range(self.game.size):
            for col in range(self.game.size):
                square = self.game.matrix[row][col]
                if self.is_winning_condition(square):
                    win_count += 1
                if self.is_blocking_condition(square):
                    block_count += 1
                if square == empty:
                    (x, y) = (row, col)

            if self.playable(win_count, (x, y)):
                self.game.setSquare(self.player_type, (x, y))
                self.first_move = False
                return True

            if self.playable(block_count, (x, y)):
                blocks.append((x, y))

            win_count = 0
            block_count = 0
            (x, y) = (-1, -1)

        for col in range(self.game.size):
            for row in range(self.game.size):
                square = self.game.matrix[row][col]
                if self.is_winning_condition(square):
                    win_count += 1
                if self.is_blocking_condition(square):
                    block_count += 1
                if square == empty:
                    (x, y) = (row, col)

            if self.playable(win_count, (x, y)):
                self.game.setSquare(self.player_type, (x, y))
                self.first_move = False
                return True

            if self.playable(block_count, (x, y)):
                blocks.append((x, y))

            win_count = 0
            block_count = 0
            (x, y) = (-1, -1)

        # top-left to bottom-right
        for d in range(self.game.size):
            square = self.game.matrix[d][d]
            if self.is_winning_condition(square):
                win_count += 1
            if self.is_blocking_condition(square):
                block_count += 1
            if square == empty:
                (x, y) = (d, d)

        if self.playable(win_count, (x, y)):
            self.game.setSquare(self.player_type, (x, y))
            self.first_move = False
            return True

        if self.playable(block_count, (x, y)):
            blocks.append((x, y))

        win_count = 0
        block_count = 0

        # bottom-left to top-right
        x = self.game.size - 1
        y = 0
        while y < self.game.size:
            square = self.game.matrix[x][y]
            if self.is_winning_condition(square):
                win_count += 1
            if self.is_blocking_condition(square):
                block_count += 1
            if square == empty:
                (x, y) = (d, d)
            x -= 1
            y += 1

        if self.playable(win_count, (x, y)):
            self.game.setSquare(self.player_type, (x, y))
            self.first_move = False
            return True

        if self.playable(block_count, (x, y)):
            blocks.append((x, y))

        if len(blocks) != 0:
            self.game.setSquare(self.player_type, blocks.pop())
            self.first_move = False
            return True

        return False

    def win(self):
        empty = ' '
        count = 0
        (x, y) = (-1, -1)

        for row in range(self.game.size):
            for col in range(self.game.size):
                square = self.game.matrix[row][col]
                if square == self.player_type:
                    count += 1
                if square == empty:
                    (x, y) = (row, col)

            if self.playable(count, (x, y)):
                self.game.setSquare(self.player_type, (x, y))
                self.first_move = False
                return True

            count = 0
            (x, y) = (-1, -1)

        for col in range(self.game.size):
            for row in range(self.game.size):
                square = self.game.matrix[row][col]
                if square == self.player_type:
                    count += 1
                if square == empty:
                    (x, y) = (row, col)

            if self.playable(count, (x, y)):
                self.game.setSquare(self.player_type, (x, y))
                self.first_move = False
                return True

            count = 0
            (x, y) = (-1, -1)

        # top-left to bottom-right
        for d in range(self.game.size):
            square = self.game.matrix[d][d]
            if square == self.player_type:
                count += 1
            if square == empty:
                (x, y) = (d, d)

        if self.playable(count, (x, y)):
            self.game.setSquare(self.player_type, (x, y))
            self.first_move = False
            return True

        count = 0

        # bottom-left to top-right
        x = self.game.size - 1
        y = 0
        while y < self.game.size:
            square = self.game.matrix[x][y]
            if square == self.player_type:
                count += 1
            if square == empty:
                (x, y) = (d, d)
            x -= 1
            y += 1

        if self.playable(count, (x, y)):
            self.game.setSquare(self.player_type, (x, y))
            self.first_move = False
            return True

        return False

    def block_opponent(self):
        empty = ' '
        count = 0
        (x, y) = (-1, -1)

        for row in range(self.game.size):
            for col in range(self.game.size):
                square = self.game.matrix[row][col]
                if square != empty and square != self.player_type:
                    count += 1
                if square == empty:
                    (x, y) = (row, col)

            if self.playable(count, (x, y)):
                self.game.setSquare(self.player_type, (x, y))
                self.first_move = False
                return True

            count = 0
            (x, y) = (-1, -1)

        for col in range(self.game.size):
            for row in range(self.game.size):
                square = self.game.matrix[row][col]
                if square != empty and square != self.player_type:
                    count += 1
                if square == empty:
                    (x, y) = (row, col)

            if self.playable(count, (x, y)):
                self.game.setSquare(self.player_type, (x, y))
                self.first_move = False
                return True

            count = 0
            (x, y) = (-1, -1)

        # top-left to bottom-right
        for d in range(self.game.size):
            square = self.game.matrix[d][d]
            if square != empty and square != self.player_type:
                count += 1
            if square == empty:
                (x, y) = (d, d)

        if self.playable(count, (x, y)):
            self.game.setSquare(self.player_type, (x, y))
            self.first_move = False
            return True

        count = 0
        (x, y) = (-1, -1)

        # bottom-left to top-right
        row = self.game.size - 1
        col = 0
        while col < self.game.size:
            square = self.game.matrix[row][col]
            if square != empty and square != self.player_type:
                count += 1
            if square == empty:
                (x, y) = (d, d)
            row -= 1
            col += 1

        if self.playable(count, (x, y)):
            self.game.setSquare(self.player_type, (x, y))
            self.first_move = False
            return True

        return False

    def play_center(self):
        if self.player_type == 'o' and self.first_move and self.game.isEmpty(self.game.center):
            self.game.setSquare(self.player_type, self.game.center)
            self.first_move = False
            return True
        return False

    def play_opposite_corner(self):
        (y, x) = self.game.last_move
        played = False

        if self.game.isCorner(self.game.last_move):
            if x != y and self.game.isEmpty((x,y)):
                self.game.setSquare(self.player_type, (x, y))
                played = True
            elif x == 0 and self.game.isEmpty((self.game.size - 1, self.game.size - 1)):
                self.game.setSquare(self.player_type, (self.game.size - 1, self.game.size - 1))
                played = True
            elif self.game.isEmpty((0, 0)):
                self.game.setSquare(self.player_type, (0, 0))
                played = True
        return played

    def play_corner(self):
        corners = [(0, 0), (0, self.game.size - 1), (self.game.size - 1, 0),
                   (self.game.size - 1, self.game.size - 1, 0)]

        for position in corners:
            if self.game.isEmpty(position):
                self.game.setSquare(self.player_type, position)
                return True
        return False

    def play_empty_side(self):
        if self.game.isEmpty((0, 1)):
            self.game.setSquare(self.player_type, (0, 1))
        if self.game.isEmpty((1, 0)):
            self.game.setSquare(self.player_type, (1, 0))
        if self.game.isEmpty((2, 1)):
            self.game.setSquare(self.player_type, (2, 1))
        if self.game.isEmpty((1, 2)):
            self.game.setSquare(self.player_type, (1, 2))

    @staticmethod
    def playable(count, position):
        return count == 2 and position[0] != -1 and position[1] != -1

    def is_winning_condition(self, square):
        return square == self.player_type

    def is_blocking_condition(self, square):
        return square != ' ' and square != self.player_type
