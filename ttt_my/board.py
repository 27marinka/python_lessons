DEFAULT_BOARD_LEN = 3
DEFAULT_BOARD_SYMBOL = '_'


# initiate board  - create matrix with defined size and symbols
def board_init(size: int = DEFAULT_BOARD_LEN, symbol: str = DEFAULT_BOARD_SYMBOL) -> list:
    result = [[symbol] * size for i in range(size)]
    return result


# print board  to user
def print_board(board: list):
    board_len = len(board)

    # print coordinates y
    coord_y = [str(i) for i in range(board_len)]
    coord_str = " ".join(coord_y)
    print(f"   {coord_str}")

    # print coordinates x + matrix strings
    for i in range(board_len):
        print(f'{str(i)} |{list_as_str(board[i])}')


# print list string to user
def list_as_str(some_list: list) -> str:
    res_str = ""
    for itm in some_list:
        res_str += str(itm) + "|"
    return res_str


# check if we have win combination on the board
def check_win(board: list) -> bool:
    # check horizontal lines
    for line in board:
        if check_line(line):
            return True
    # check vertical lines
    transponded_board = zip(*board)
    for line in transponded_board:
        if check_line(line):
            return True

    # check diagonales
    diagonal1 = []
    diagonal2 = []
    board_len = len(board)
    for i in range(board_len):
        diagonal1.append(board[i][i])
        diagonal2.append(board[board_len - i - 1][i])
    if check_line(diagonal1) or check_line(diagonal2):
        return True

    return False


# returns True if all symbols in the list are the same , and not the default
def check_line(line: list) -> bool:
    lineset = set(line)
    if len(lineset) == 1 and not(DEFAULT_BOARD_SYMBOL in lineset):
        return True
    else:
        return False

