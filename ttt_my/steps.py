import random
from ttt_my.board import print_board, check_win, DEFAULT_BOARD_SYMBOL


# steps of users one by one until win or drawn
def users_steps(users: dict, board: list) -> str:
    step_number = 0
    while True:
        for itm, name in enumerate(users):
            symbol = users[name][0]
            mode = users[name][1]
            step_number += 1
            print(f'Step {step_number}. =============================================')
            if mode == '1':
                step = comp_step(name, symbol, board)
            elif mode == '2':
                step = user_step(name, symbol, board)

            board[step[0]][step[1]] = symbol
            print_board(board)

            is_win = check_win(board)
            if is_win:
                result_string = f'Player {name} won on the step {step_number} ! Congratulations!'
                return result_string

            elif step_number > 8:
                result_string = f'Drawn game'
                return result_string


# put symbol on the board
def user_step(name: str, symbol: str, board: list) -> tuple:
    while True:
        step_coord = tuple(input(f'Player {name}, your turn (symbol {symbol}). Please input coordinates without whitespace:\n'))
        try:
            x = int(step_coord[0])
            y = int(step_coord[1])
            if check_step(x, y, board):
                return x, y
            else:
                print("Step is impossible, the cell is already occupied")
        except (KeyError, IndexError, ValueError):
            print("Step is impossible, please input coordinates without whitespace")
    return False


# check if step is possible - when the cell is empty
def check_step(x: int, y: int, board: list) -> bool:
    cell = board[x][y]
    if cell == DEFAULT_BOARD_SYMBOL:
        return True
    else:
        return False


# random step of the COMP
def comp_step(name: str, symbol: str, board: list) -> tuple:
    all_steps = get_all_possible_steps(board)
    random_step = random.choice(all_steps)
    print(f"Player {name} (symbol {symbol}) made a move")
    return random_step


# get all possible steps on the board - for COMP step
def get_all_possible_steps(board: list) -> list:
    all_steps = []
    for x, line in enumerate(board):
        for y, sell in enumerate(line):
            if board[x][y] == DEFAULT_BOARD_SYMBOL:
                all_steps.append((x, y))
    return all_steps






