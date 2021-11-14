class Board:

    # size - размер доски
    # содержимое таблица доски (матрица)
    # выбывшие ячейки в виде кортежей
    # Отображение доски
    # Принять ход
    # Проверка на матчинг

    # TODO: Создать класс реализующий доску для игры в крестики нолики
    # TODO: Метод установки шага на доску
    # TODO: Метод проверки что есть победитель
    # TODO: Метод печати доски на экран

    def __init__(self, size: int, symbol: str):
        self.size = size,
        self.symbol = symbol
        self.all_steps = set((n, m) for n in range(self.size) for m in range(self.size))
        self.done_steps = set()
        self.signs_on_board = [[self.symbol for _ in range(self.size)] for _ in range(self.size)]

    def print_board(self):
        pass

    def add_step(self, step: tuple):
        pass

    def chek(self) -> bool:
        pass


board1 = Board(3, '0')

print(board1.size)
print(board1.symbol)


