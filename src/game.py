from game.GameBoard import GameBoard
from game.GameField import GameField
from game.Snake import Snake


def generate_game_board(rows, columns):
    game_board = []
    for row in range(rows):
        for col in range(columns):
            game_board.append(GameField("empty", row, col))
    return game_board


def generate_snake():
    starting_position = [(2, 3), (3, 3), (4, 3)]

    player = Snake(
        starting_position=starting_position,
        head_position=starting_position[0],
        facing_direction="UP",
        speed=1,
    )
    return player


def generate_food(rows, columns):
    return None


def update_game_board(game_board, snake, food):
    return game_board
