# нарисуем доску, спросим ход
from hometasks.ttt_my.board import board_init, print_board
from hometasks.ttt_my.userinterface import introduction


def start_game():
    users = {}
    try:
        users = introduction('en')

    except "ValueError":





    board = board_init()
    print_board(board)


start_game()

