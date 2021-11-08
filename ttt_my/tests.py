from ttt_my.board import check_win, board_init, print_board


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


#usertest = {'Marina': 'X', 'Kate': 'O'}
#boardtest = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
#users_steps(usertest, boardtest)


