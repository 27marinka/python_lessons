"""
Имеется 2 кортежа с координатами Ферзя и Пешки на шахматной доске
Определить Бьет ли Ферзь пешку
координаты хранятся (x, y)
"""

ferze = (1, 3)
peshka = (4, 6)


if ferze[0] == peshka[0] or ferze[1] == peshka[1]:
    print('YES!')
else:
    mod_x = abs(ferze[0]-peshka[0])
    mod_y = abs(ferze[1]-peshka[1])
    if mod_x == mod_y:
        print('YES!')
    else:
        print('NO')
