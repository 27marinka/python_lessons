import random

from OOP.boardclass import Board

COMP_NAMES = ['Garry Potter', 'Hermione Granger', 'Dobby', 'Lord Voldemort', 'Draco Malfoy', 'Albus Dumbledore']


class Player:

    def __init__(self, symbol, name=None):
        self.symbol = symbol
        self.name = self._get_name(name)

    def _get_name(self, name):
        if name:
            return name
        return random.choice(COMP_NAMES)

    # random step of the COMP
    def comp_step(self, board: list) -> tuple:
        all_steps = board.all_possible_steps
        random_step = random.choice(all_steps)
        print(f"Player {self.name} (symbol {self.symbol}) made a move")
        return random_step


class Gamer(Player):

    def _get_name(self, name):
        if name:
            return name
        user_input = input(f"Please enter the name of the player (symbol {self.symbol}):\n")
        return user_input

    def user_step(self, board: Board) -> tuple:
        while True:
            step_coord = tuple(
                input(
                    f'Player {self.name}, your turn (symbol {self.symbol}). Please input coordinates without whitespace:\n'))
            try:
                x = int(step_coord[0])
                y = int(step_coord[1])
                if board.check_step(x, y):
                    return x, y
                else:
                    print("Step is impossible, the cell is already occupied")
            except (KeyError, IndexError, ValueError):
                print("Step is impossible, please input coordinates without whitespace")
        return False

