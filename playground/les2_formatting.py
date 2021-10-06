dog = "Шарик"
action = "Играет"
toy = "Мячик"

dog.upper()


form1 = "{0} {1} в {2}"
res = form1.format(dog.upper(), action, toy)
print(res.capitalize())

form2 = "{0},{1},{2},{3},{4}"
res2 = form2.format(*dog)
print(res2)

razd = res.split()
print(razd)
