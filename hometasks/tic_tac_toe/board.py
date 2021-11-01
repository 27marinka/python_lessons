def get_board(size):
    result = []
    for _ in range(size):
        row = []
        for _ in range(size):
            row.append(0)
        result.append(row)
    return result


def board_match(board):
    def chek_line(line):
        line_set = set(line)
        if (0 not in line_set and len(line_set) == 1):
            raise ValueError("CHECK_LINE")
        return False

    board_len = len(board)
    diagonal = map(lambda idx: board[idx][idx], range(0, board_len))
    diagonal_invert = map(lambda idx: board[idx][board_len - idx - 1], range(board_len - 1, -1, -1))
    try:
        _ = any(map(chek_line, (diagonal, diagonal_invert)))
        for row, column in zip(board, zip(*board)):
            _ = any(map(chek_line, (row, column)))
    except ValueError as exc:
        if 'CHECK_LINE' in exc.args:
            return True
        else:
            raise exc
    return False


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
