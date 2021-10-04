"""
2. Задание
Даны данные человека
"""
import datetime

name = "Василий"
surname = "Иванов"
age = 33
height = 182

now = datetime.datetime.now()
current_year = now.year

birth_year = current_year - age
bio = name + ' ' + surname + ' ' + str(birth_year) + ' ростом ' + str(height) + ' см'
print(bio)
print('the end')

# вычислить Год рождения (относительно текущего года) и присвоить переменной birth_year
# Составить строку по шаблону {name} {surname} {birth_year} ростом {height} см и присвоить переменной bio
# Напечатать на экране значение bio