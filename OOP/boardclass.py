from itertools import product

class Board:
    # size - размер доски
    # содержимое таблица доски (матрица)
    # Отображение доски
    # Принять ход
    # Проверка на матчинг

    # TODO: Создать класс реализующий доску для игры в крестики нолики
    # TODO: Метод установки шага на доску
    # TODO: Метод проверки что есть победитель
    # TODO: Метод печати доски на экран

    def __init__(self, size: int, symbol: str):
        self.size = size
        self.symbol = symbol
        self.board = [[symbol for _ in range(self.size)] for _ in range(self.size)]
        self.all_possible_steps = tuple(product(range(3), range(3)))
        # self.all_possible_steps = set((n, m) for n in range(self.size) for m in range(self.size))
       # self.done_steps = set()

    def print_board(self):
        # print coordinates y
        coord_y = [str(i) for i in range(self.size)]
        coord_str = " ".join(coord_y)
        print(f"   {coord_str}")
        # print coordinates x + matrix strings
        for i in range(self.size):
            print(f'{str(i)} |{self.__list_as_str(self.board[i])}')

    # print list string to user
    def __list_as_str(self, line: list) -> str:
        res_str = ""
        for itm in line:
            res_str += str(itm) + "|"
        return res_str

    # check if step is possible - when the cell is empty
    def check_step(self, x: int, y: int) -> bool:
        cell = self.board[x][y]
        if cell == self.symbol:
            return True
        else:
            return False

    # check if we have win combination on the board
    def check_win(self) -> bool:
        # check horizontal lines
        for line in self.board:
            if self.__check_line(line):
                return True
        # check vertical lines
        transponded_board = zip(*self.board)
        for line in transponded_board:
            if self.__check_line(line):
                return True
        # check diagonales
        diagonal1 = []
        diagonal2 = []
        for i in range(self.size):
            diagonal1.append(self.board[i][i])
            diagonal2.append(self.board[self.size - i - 1][i])
        if self.__check_line(diagonal1) or self.__check_line(diagonal2):
            return True

        return False

    # returns True if all symbols in the list are the same , and not the default
    def __check_line(self, line: list) -> bool:
        lineset = set(line)
        if len(lineset) == 1 and not (self.symbol in lineset):
            return True
        else:
            return False


board1 = Board(3, '0')

print(board1.size)
print(board1.symbol)
board1.print_board()

print(board1.check_win())



