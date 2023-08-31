from game.GameBoard import GameBoard
from game.GameField import GameField
from game.Snake import Snake
import numpy as np
import random


def generate_game_board(rows, columns):
    game_board = []
    for row in range(rows):
        for col in range(columns):
            if row == 0 or row == rows - 1 or col == 0 or col == columns - 1:
                game_board.append(GameField("edge", row, col))
            else:
                game_board.append(GameField("empty", row, col))
    return game_board


def generate_snake(game_board):
    starting_position = [(2, 3), (3, 3), (4, 3)]

    player = Snake(
        list_snake_fields=starting_position,
        head_position=starting_position[0],
        facing_direction=(0, -1),
        speed=1,
    )

    return player


# Facing directions: (0, -1) = UP    (0, 1) = DOWN   (-1, 0) = LEFT  (1, 0) = RIGHT


def generate_food(game_board, height, width):
    existing_food_field = (
        (
            index
            for index, game_field in enumerate(game_board)
            if game_field.status == "food"
        ),
        None,
    )

    if existing_food_field != None:
        return game_board

    food_position = (random.randint(1, width - 1), random.randint(1, height - 1))

    if get_game_field(food_position).status == "empty":
        indice = next(
            (
                index
                for index, game_field in enumerate(game_board)
                if game_field.position == food_position
            ),
            None,
        )
        game_board[indice].position = food_position
        game_board[indice].status = "food"
    else:
        generate_food(game_board, height, width)
    return game_board


def print_board(game_board):
    print("Printing game board:")
    for value in game_board:
        print(f"{value.row} {value.column} {value.status}")
    return None


def update_game_board(game_board, snake, food):
    return game_board


def move_snake(snake, food):
    new_position = snake.list_snake_fields[0] + snake.facing_direction
    snake.list_snake_fields.insert(0, new_position)

    # Grow snake in case new position equals food position
    if new_position != food.position:
        snake.list_snake_fields.pop()

    return snake


def check_game_state(game_board, snake):
    current_field = get_game_field(game_board, snake.list_snake_fields[0])
    if current_field.status == "edge" or current_field.status == "snake":
        return False

    return True


def get_game_field(game_board, target_position):
    current_field = next(
        (
            field
            for row in game_board
            for field in row
            if field.position == target_position
        ),
        None,
    )

    if current_field == None:
        raise ValueError("No field found")

    return current_field


def wait_for_player():
    return None


def game_over():
    print("Game over!")
    quit()


def game_loop():
    game_board = generate_game_board(16, 16)
    snake = generate_snake()
    food = generate_food()
    # update_game_board(game_board, snake, food)
    # print_board(game_board)

    while check_game_state(game_board, snake):
        generate_food(game_board)
        move_snake(snake, food)
        wait_for_player()

    game_over()


game_loop()
