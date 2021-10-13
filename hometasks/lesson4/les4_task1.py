import random
"""
Даны матрицы n на m
Матрица олицетворяет улицу, колонки в Матрице олицетворяют Здания. 1 в колонке означает наличие этажа, 0 его отсутвие
Написать алгоритм нахождения самого высокого здания на улице. результат сохранить в переменную в виде кортежа или
списка [номер колонки, количество этажей]
"""
"""
пример матрицы:
some_builds = [
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [1, 1, 1, 0],
    [1, 1, 1, 1]
]
результат для данной матрицы = [3, 4] 3 - колонка, 4 - высота здания
"""

# if we need to create random matrix
"""
row_count = random.randint(2, 11)
col_count = random.randint(2, 11)

some_buildings = []


for i in range(row_count):
    some_buildings.append([])
    for j in range(col_count):
        floor = random.randint(0, 1)
        some_buildings[i].append(floor)

"""

some_buildings = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1]
]

row_count = len(some_buildings)
col_count = len(some_buildings[0])

print("rows = " + str(row_count))
print("cols = " + str(col_count))

print("BUILDINGS MATRIX:")
for item in some_buildings:
    print(item)

buildings_result = []
max_floor = 0

for col in range(0, col_count):
    floors_count = 0
    for row in range(0, row_count):
        floors_count += some_buildings[row][col]
    if max_floor < floors_count:
        max_floor = floors_count
        column = col + 1
        buildings_result = [column, max_floor]

print("="*15)
print("result [building, floor_count]:")
print(buildings_result)
