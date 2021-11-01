DEFAULT_BOARD_LEN = 3
DEFAULT_BOARD_SYMBOL = '_'


# initiate board  - create
def board_init(size: int = DEFAULT_BOARD_LEN, symbol: str = DEFAULT_BOARD_SYMBOL) -> list:
    row = [symbol for _ in range(size)]
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
       print(f'{str(i)} |{list_as_str(board[i])}')


def list_as_str(some_list) -> str:
    res_str = ""
    for itm in some_list:
        res_str += str(itm) + "|"
    return res_str


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


test_board()
