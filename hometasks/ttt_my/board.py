DEFAULT_BOARD_LEN = 3


# initiate board  - create
def board_init(size: int = DEFAULT_BOARD_LEN) -> list:
    row = ['_' for _ in range(size)]
    result = [row for _ in range(size)]
# result = [[0 for _ in range(3)] for _ in range(3)]
    return result


# print board  to user
def print_board(board: list) -> None:
    # размер борда
    board_len = len(board)
    # нужно вывести верхнюю строку координат

    # variant 1
    # coord_str = ""
    #  for i in range(board_len):
    #    coord_str += str(i) + " "

    # variant 2 мне кажется этот лучше.
    coord_y = [str(i) for i in range(board_len)]
    coord_str = " ".join(coord_y)

    print(f"   {coord_str}")

    # нужно вывести вертикальную строку координат + строку борда
    for i in range(board_len):
        print(f"{str(i)} |{str('|'.join(board[i]))}|")


def test_board():
    board = board_init(1)
    print_board(board)

    board = board_init(2)
    print_board(board)

    board = board_init(3)
    print_board(board)

    board = board_init(4)
    print_board(board)

    board = board_init(5)
    print_board(board)

    board = board_init(8)
    print_board(board)


# test_board()