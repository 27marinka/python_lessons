"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
"""

month = int(input("Please input month number >> "))

time_ofyear = {
    "Winter": (12, 1, 2),
    "Spring": (3, 4, 5),
    "Summer": (6, 7, 8),
    "Autumn": (9, 10, 11)
}

if 1 <= month <= 12:
    for items in time_ofyear.items():
        time = items[0]
        if month in items[1]:
            print("The time of year is >> " + time)
            break
else:
    print("Incorrect month number. Please input number from 1 to 12")

