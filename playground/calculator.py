import sys
from colorama import Fore, Back, Style
"""
Прикольный калькулятор
запестите файл с аргументами - целыми числами. 
Также работает help или -h
"""


def fun_sum(args) -> str:
    res = sum(args)
    fun_res = f'Я тут все сложил за тебя, и вышло:  {res}'
    return fun_res


def fun_multiple(args) -> str:
    res = 1
    for i in args:
        res = res * i
    fun_res = f'Фуух, перемножил... {res}'
    return fun_res


def main():
    program_args = sys.argv
    input_args = program_args[1:]
    try:
        int_args = map(int, input_args)
        if len(list(int_args)) == 0:
            calculator_help()
        else:
            print_results(int_args)
    except ValueError:
        if input_args.count('-h') > 0 or input_args.count('help') > 0:
            calculator_help()
        else:
            print("Неверный ввод")
            calculator_help()


def calculator_help():
    print(Fore.CYAN)
    print("Чтобы воспользоваться прикольным калькулятором, введите числа через пробел")
    print(Fore.RESET)


def print_results(args):
    print(Fore.MAGENTA)
    print(fun_sum(args))
    print(fun_multiple(args))
    print(Fore.RESET)


main()
