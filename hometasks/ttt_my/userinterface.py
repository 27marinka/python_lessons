PHRASES = {
    "want": {'ru': 'Привет! Хочешь поиграть в крестики - нолики ?\nВведи Y, если хочешь, если нет - любой другой символ\n',
             'en': 'Hi! Do you want to play tic tac toe?\nEnter Y, if you want, if no - any other symbol\n'},
    "name_first": {'ru': 'Введи имя 1-го игрока\n',
                   'en': 'Please enter the name of the first player\n'},
    "name_second": {'ru': 'Введи имя 2-го игрока\n',
                    'en': 'Please enter the name of the second player\n'},
    "bye": {'ru': 'Пока!',
            'en': 'Good bye'},
    "started": {'ru': 'Игра начинается!',
                'en': 'The game is started'}
}


def introduction(lang: str)-> dict:
    want_to_start = input(PHRASES["want"][lang])
    if want_to_start == 'Y':
        name1 = input(PHRASES["name_first"][lang])
        name2 = input(PHRASES["name_second"][lang])
        users = {
            name1: "X",
            name2: "O"
        }
        print(PHRASES["started"][lang])
        return users
    else:
        print(PHRASES["bye"][lang])


introduction('en')