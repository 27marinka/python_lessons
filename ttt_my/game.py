from ttt_my.board import board_init, print_board
from ttt_my.logging import log_game, create_log_startstring, get_session_number
from ttt_my.steps import users_steps
from ttt_my.userinterface import introduction
from colorama import Fore


# creates users, get session number and starts game.
def init_game():
    users = introduction()
    gamesession = get_session_number()
    start_game(users, gamesession)


# show board to user, show  results of the game, logging games and possibility to play with the same players once more
def start_game(users: dict, gamesession: int):

    log_starstring = create_log_startstring(gamesession, users)

    board = board_init()
    print_board(board)

    result = users_steps(users, board)
    show_results(result)
    log_game(log_starstring, result)

    one_more_game = input('Do you want to play once more? (Y/N)').upper()
    if one_more_game == 'Y':
        gamesession += 1
        start_game(users, gamesession)
    else:
        print("bye")


# show results of the game to the user
def show_results(result: str):
    print(Fore.CYAN)
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(result)
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(Fore.RESET)
