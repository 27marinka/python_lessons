# creates users, get session number and starts game.
from OOP.boardclass import Board
from OOP.playerclass import Gamer

def init_game():
    board = Board(3, '_')
    user1 = Gamer("X")
    user2 = Gamer("O")


init_game()

