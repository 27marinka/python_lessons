import sys
import random

PHRASES = {
    "hello": {'ru': 'Привет! начинаем игру в крестики - нолики!\n',
              'en': 'Hi! Start playing tic-tac-toe!\n'},
    "name_first": {'ru': 'Введи имя 1-го игрока (X)\n',
                   'en': 'Please enter the name of the first player (X)\n'},
    "name_second": {'ru': 'Введи имя 2-го игрока (O)\n',
                    'en': 'Please enter the name of the second player (O)\n'},
    "bye": {'ru': 'Пока!\n',
            'en': 'Good bye\n'},
    "started": {'ru': 'Игра начинается!\n',
                'en': 'The game is started\n'},
    "mode": {'ru': 'Выберите режим игры. 1 - с КОМПЬЮТЕРОМ, 2 - с ДРУГИМ ИГРОКОМ\n',
             'en': 'Please choose the game mode. 1 - COMP, 2 - USER\n'},
    "compname": {'ru': 'Вы играете против игрока ',
             'en': 'You are playing with '}
}

GAME_MODE = {
    '1': "COMP",
    '2': "USER"
}


def introduction(lang: str) -> dict:
    print(PHRASES["hello"][lang])
    # arguments
    program_args = sys.argv
    input_args = program_args[1:]
    # save game mode
    try:
        mode_name = GAME_MODE[input_args[0]]
        mode_id = input_args[0]
        print(f'Game mode is {mode_name}')
    except (KeyError, IndexError):
        mode_id = input(PHRASES["mode"][lang])
    # save name 1
    try:
        name1 = input_args[1]
    except IndexError:
        name1 = input(PHRASES["name_first"][lang])
    # save name 2 (or generate comp name)
    try:
        name2 = input_args[2]
    except IndexError:
        if mode_id == '2':
            name2 = input(PHRASES["name_second"][lang])
        else:
            name2 = get_random_name()
            print(f'{PHRASES["compname"][lang]} {name2}')

    users = {
        name1: ["X", "2"],
        name2: ["O", mode_id]
    }

    print(PHRASES["started"][lang])
    return users



def get_random_name() -> str:
    comp_names = ['Garry Potter', 'Hermione Granger', 'Dobby', 'Lord Voldemort', 'Draco Malfoy', 'Albus Dumbledore']
    random_name = random.choice(comp_names)
    return random_name

# introduction('en')