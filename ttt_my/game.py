"""
может принимать аргументы: 
1 - режим игры (COMP/USERS), 
2 - имя игрока 1
3 - имя игрока 2
"""
import ttt_my
from ttt_my.board import board_init, print_board
from ttt_my.steps import users_steps
from ttt_my.userinterface import introduction
from colorama import Fore, Back, Style


def init_game():
    users = introduction('en')
    start_game(users)


def start_game(users: dict):
    board = board_init()
    print_board(board)

    result = users_steps(users, board)
    show_results(result)

    one_more_game = input('Хотите сыграть еще? (Y/N)').upper()
    if one_more_game in ['Y', 'N']:
        if one_more_game == 'Y':
            start_game(users)
        else:
            print("bye")
    else:
        print("bye")


def show_results(result: str):
    print(Fore.CYAN)
    print("+++++++++++++++++++++++++++++++++++++++")
    print(result)
    print("+++++++++++++++++++++++++++++++++++++++")
    print(Fore.RESET)
