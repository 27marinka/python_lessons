"""
1. Задание
дана переменная
"""
dog = "Шарик"
action = "Играет"
toy = "Мячик"

shablon = "{0} {1} в {2}"
print(shablon.format(dog, action, toy))

print(f"{dog} {action} в {toy}")

# напечатать на экране фразу по шаблону {dog} {action} в {toy}