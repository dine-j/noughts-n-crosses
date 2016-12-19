from game import AiGenerator
from game import Board


def main():
    game = Board()
    ai = AiGenerator(game, 'o', "perfect")

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


if __name__ == "__main__": main()
