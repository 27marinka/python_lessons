"""
Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
пример списка: [22, 11, 45, 87, 0, 1, 6]
результат работы алгоритма с данным списком: [11, 22, 87, 45, 1, 0, 6]
будьте внимательны, пользователь необзательно в качестве значений введет числа, преобразованием и проверками
заниматься не надо, только разделить то что ввел пользователь и получить список значений.
"""

user_list = []
more_input = 1

while more_input:
    item = input(">>")
    user_list.append(item)
    more = input("Do you want to enter one more item? (Y/N) >>")
    if more.upper() != 'Y':
        more_input = 0
        print("Input finished")


print("user_list before:")
print(user_list)

num = 0
list_len = len(user_list)

while num < (list_len - 1):
    user_list[num], user_list[num + 1] = user_list[num + 1], user_list[num]
    num += 2

print("user_list after:")
print(user_list)

