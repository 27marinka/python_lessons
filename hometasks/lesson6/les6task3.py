""" 3
На вход функции подается строка, вернуть булевое является эта строка полиндромом или нет
проверочная строка "Пал, а норов худ и дух ворона лап."
Полиндром это строка которая читается в обе стороны одинаково, при этом знаки препинания числа и непечатные символы
игнорируются
"""

input_string = "Пал, а норов худ и дух ворона лап."



def is_palindrome(my_str):
    formatted_str = my_str.lower()
    new_string = []
    for lit in list(formatted_str):
        if lit.isalnum():
            new_string.append(lit)
    return new_string == new_string[::-1]



print(is_palindrome(input_string))