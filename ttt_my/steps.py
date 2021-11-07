# приглавшение для игрока 1 ввести ход + показ доски
# проверка хода на корректность
# простоавление хода на доске
# проверка, выиграл ли кто-то
# ход следующего игрока
import random

from ttt_my.board import print_board, check_win, DEFAULT_BOARD_SYMBOL


def users_steps(users: dict, board: list) -> str:
    step_number = 0
    while True:
        for itm, name in enumerate(users):
            symbol = users[name][0]
            mode = users[name][1]
            step_number += 1
            print(f'Ход {step_number}. =================================')
            if mode == '1':
                step = comp_step(name, symbol, board)
            elif mode == '2':
                step = user_step(name, symbol, board)

            board[step[0]][step[1]] = symbol
            print_board(board)

            is_win = check_win(board)
            if is_win:
                result_string = f'Победа игрока {name} на ходу {step_number}'
                return result_string

            elif step_number > 8:
                result_string = f'Ничья'
                return result_string


def user_step(name: str, symbol: str, board: list):
    # проставляем символ на доску
    while True:
        step_coord = tuple(input(f'Игрок {name}, ваш ход (символ {symbol}). Ввведите координаты без пробела:\n'))
        try:
            x = int(step_coord[0])
            y = int(step_coord[1])
            if check_step(x, y, board):
                #board[x][y] = symbol
                return (x, y)
            else:
                print("ход невозможен, ячейка уже занята")
        except (KeyError, IndexError, ValueError):
            print("ход невозможен, введите координаты без пробела")
    return False


def check_step(x: int, y: int, board: list) -> bool:
    cell = board[x][y]
    if cell == DEFAULT_BOARD_SYMBOL:
        return True
    else:
        return False


def comp_step(name: str, symbol: str, board: list) -> tuple:
    all_steps = get_all_possible_steps(board)
    random_step = random.choice(all_steps)

    print(f"Игрок {name} (символ {symbol}) совершил ход")
    return random_step



def get_all_possible_steps(board: list) -> list:
    all_steps = []
    for x, line in enumerate(board):
        for y, sell in enumerate(line):
            if board[x][y] == DEFAULT_BOARD_SYMBOL:
                all_steps.append((x, y))
    return all_steps


#usertest = {'Marina': 'X', 'Kate': 'O'}
#boardtest = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
#users_steps(usertest, boardtest)




