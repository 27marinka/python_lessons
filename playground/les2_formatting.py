from colorama import Fore, Back, Style


print(Back.GREEN + 'and with a green background')
print(Fore.BLACK + 'some black text')



print(Back.CYAN )

dog = "Шарик"
action = "Играет"
toy = "Мячик"

dog.upper()


form1 = "{0} {1} в {2}"
res = form1.format(dog.upper(), action, toy)
print(res.capitalize())

print(Back.RED )
form2 = "{0},{1},{2},{3},{4}"
res2 = form2.format(*dog)
print(res2)

print(Back.YELLOW )
razd = res.split()
print(razd)

x = 44.66
