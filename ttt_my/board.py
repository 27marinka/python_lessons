DEFAULT_BOARD_LEN = 3
DEFAULT_BOARD_SYMBOL = '_'


# initiate board  - create
def board_init(size: int = DEFAULT_BOARD_LEN, symbol: str = DEFAULT_BOARD_SYMBOL) -> list:
    result = [[symbol] * size for i in range(size)]
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


def check_win(board) -> bool:
    # проверка горизонтальных строк
    for line in board:
        if check_line(line):
            return True
    # проверка вертикальных строк (нужно транспонировать матрицу)
    transponded_board = zip(*board)
    for line in transponded_board:
        if check_line(line):
            return True

    # проверка диагоналей
    diagonal1 = []
    diagonal2 = []
    board_len = len(board)
    for i in range(board_len):
        diagonal1.append(board[i][i])
        diagonal2.append(board[board_len - i - 1][i])
    # проверка диагонали 1
    if check_line(diagonal1) or check_line(diagonal2):
        return True

    return False



def check_line(line):
    lineset = set(line)
    if len(lineset) == 1 and not(DEFAULT_BOARD_SYMBOL in lineset):
        return True
    else:
        return False


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


#test_board()

def test_checkwin():
    matrix_tests = (
        (([1, 1, 1],
          [0, 0, 0],
          [0, 0, 0]), True),

        (([1, 0, 0],
          [1, 0, 1],
          [1, 0, 0]), True),

        (([2, 0, 0],
          [0, 2, 0],
          [2, 0, 2]), True),

        (([0, 1, '_'],
          [0, 0, 1],
          [1, 1, '_']), False),

        (([1, 0, 0],
          [1, 0, 0],
          [1, 0, 0]), True),

        (([0, 1, 0],
          [0, 1, 0],
          [0, 1, 0]), True),

        (([0, 0, 2],
          [0, 0, 2],
          [0, 0, 2]), True),
        ((['_', '_', '_'],
          [0, 1, '_'],
          [0, 0, 1]), False),
        (([1, 1, 2],
          [0, 1, 2],
          [0, 0, 1]), True),
        (([2, 1, 1],
          [2, 1, 2],
          [1, '_', 1]), True),
    )

    for test in matrix_tests:
        assert check_win(test[0]) is test[1], test[0]


#test_checkwin()


