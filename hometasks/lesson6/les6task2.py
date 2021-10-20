"""2
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
"""

input_list = [6, 6, 4, 6, 7, 5, 9, 4, 1, 7, 4]
result_list = []

# define function
def get_unique_number(data_list):
    # get each element of a list
    for num in data_list:
        # count number of occurencies of current number in tha list
        occur = data_list.count(num)
        # if 1 occurence - unique
        if occur == 1:
            # return and stop
            yield num

#get all values that function generator returns
for next_num in get_unique_number(input_list):
    # add value to the list
    result_list.append(next_num)

print("List of unique numbers: ")
print(result_list)
