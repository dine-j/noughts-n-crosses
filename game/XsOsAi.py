from abc import ABCMeta, abstractmethod
from random import randint


class Ai:
    __metaclass__ = ABCMeta

    def __init__(self, game, player_type):
        self.game = game
        self.player_type = player_type

    @abstractmethod
    def play(self):
        pass

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
                self.game.set_square(self.player_type, (x, y))
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
                self.game.set_square(self.player_type, (x, y))
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
            self.game.set_square(self.player_type, (x, y))
            return True

        if self.playable(block_count, (x, y)):
            blocks.append((x, y))

        if len(blocks) != 0:
            self.game.set_square(self.player_type, blocks.pop())
            return True

        return False

    @staticmethod
    def playable(count, position):
        return count == 2 and position[0] != -1 and position[1] != -1

    def is_winning_condition(self, square):
        return square == self.player_type

    def is_blocking_condition(self, square):
        return square != ' ' and square != self.player_type


class RandomAi(Ai):
    def __init__(self, game, player_type):
        super(RandomAi, self).__init__(game, player_type)

    def play(self):
        x = randint(0, 2)
        y = randint(0, 2)
        while not self.game.is_empty((x, y)):
            x = randint(0, 2)
            y = randint(0, 2)
        self.game.set_square(self.player_type, (x, y))


class AverageAi(Ai):
    def __init__(self, game, player_type):
        super(AverageAi, self).__init__(game, player_type)

    def play(self):
        if self.fill_third_space():
            return
        x = randint(0, 2)
        y = randint(0, 2)
        while not self.game.is_empty((x, y)):
            x = randint(0, 2)
            y = randint(0, 2)
        self.game.set_square(self.player_type, (x, y))


class PerfectAi(Ai):
    def __init__(self, game, player_type):
        super(PerfectAi, self).__init__(game, player_type)
        self.first_move = True

    def play(self):
        if self.fill_third_space():
            self.first_move = False
            print("fill third space")
            return

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

    def play_center(self):
        if self.player_type == 'o' and self.first_move and self.game.is_empty(self.game.center):
            self.game.set_square(self.player_type, self.game.center)
            self.first_move = False
            return True
        return False

    def play_opposite_corner(self):
        (y, x) = self.game.last_move
        played = False

        if self.game.is_corner(self.game.last_move):
            if x != y and self.game.is_empty((x, y)):
                self.game.set_square(self.player_type, (x, y))
                played = True
            elif x == 0 and self.game.is_empty((self.game.size - 1, self.game.size - 1)):
                self.game.set_square(self.player_type, (self.game.size - 1, self.game.size - 1))
                played = True
            elif self.game.is_empty((0, 0)):
                self.game.set_square(self.player_type, (0, 0))
                played = True
        return played

    def play_corner(self):
        corners = [(0, 0), (0, self.game.size - 1), (self.game.size - 1, 0),
                   (self.game.size - 1, self.game.size - 1, 0)]

        for position in corners:
            if self.game.is_empty(position):
                self.game.set_square(self.player_type, position)
                return True
        return False

    def play_empty_side(self):
        if self.game.is_empty((0, 1)):
            self.game.set_square(self.player_type, (0, 1))
        if self.game.is_empty((1, 0)):
            self.game.set_square(self.player_type, (1, 0))
        if self.game.is_empty((2, 1)):
            self.game.set_square(self.player_type, (2, 1))
        if self.game.is_empty((1, 2)):
            self.game.set_square(self.player_type, (1, 2))
