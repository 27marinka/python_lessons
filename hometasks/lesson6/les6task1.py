"""Представлен список чисел.
Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Для формирования списка использовать генератор.
"""

input_list = [4, 6, 35, 56, 23, 5, 9, 4, 44, 100, 8]
result_list = []

# define function
def get_greater_number(data_list):
    # get each element of a list + index
    for ind, num in enumerate(data_list, 0):
        try:
            # don't compare 1st[0] elemet , curent element > previouse
            if ind != 0 and num > data_list[ind - 1]:
                # return num and stop
                yield num
        except "IndexError":
            print("KeyErr")

#get all values that function generator returns
for next_num in get_greater_number(input_list):
    #add value to the list
    result_list.append(next_num)

print("List of unique numbers: ")
print(result_list)