from game import AiGenerator
from game import Board


def main():
    game = Board()
    ai = AiGenerator(game, 'o', "perfect")

    # 1
    game.matrix = [['x', ' ', 'x'],
                   [' ', ' ', ' '],
                   ['o', 'x', 'o']]
    game.last_move = (2, 1)
    game.last_piece = 'x'

    answer = [['x', 'o', 'x'],
              [' ', ' ', ' '],
              ['o', 'x', 'o']]

    ai.play()
    assert (game.matrix == answer)

    # 2
    game.matrix = [['x', ' ', 'x'],
                   ['x', 'o', ' '],
                   ['o', ' ', ' ']]
    game.last_move = (0, 2)
    game.last_piece = 'x'

    answer = [['x', 'o', 'x'],
              ['x', 'o', ' '],
              ['o', ' ', ' ']]
    ai.play()
    assert (game.matrix == answer)

    # 3
    game.matrix = [['x', 'o', 'x'],
                   ['x', 'o', 'x'],
                   ['o', ' ', ' ']]
    game.last_move = (1, 2)
    game.last_piece = 'x'

    answer = [['x', 'o', 'x'],
              ['x', 'o', 'x'],
              ['o', 'o', ' ']]
    ai.play()
    assert (game.matrix == answer)

    # 4
    game.matrix = [[' ', ' ', ' '],
                   [' ', 'x', ' '],
                   [' ', ' ', ' ']]
    game.last_move = (1, 1)
    game.last_piece = 'x'

    answer1 = [['o', ' ', ' '],
               [' ', 'x', ' '],
               [' ', ' ', ' ']]

    answer2 = [[' ', ' ', ' '],
               [' ', 'x', ' '],
               [' ', ' ', 'o']]

    answer3 = [[' ', ' ', 'o'],
               [' ', 'x', ' '],
               [' ', ' ', ' ']]

    answer4 = [[' ', ' ', ' '],
               [' ', 'x', ' '],
               ['o', ' ', ' ']]
    ai.play()
    assert (game.matrix == answer1 or game.matrix == answer2 or game.matrix == answer3 or game.matrix == answer4)


if __name__ == "__main__": main()
