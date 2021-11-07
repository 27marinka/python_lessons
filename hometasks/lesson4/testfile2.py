my_list = ["cat", "dog", "rat"]

for animal in my_list:
    print(animal)
    print("-"*10)
else:
    print("the end")

for n in range(3, 6):
    print(n)

ran = range(4, 24)

print(type(ran))
print(ran)

print(list(range(0, 41)))

listzip = list(zip(my_list, ran))

print(listzip)

home1 = [1, 0, 0, 0, 0]
home2 = [1, 1, 1, 1, 0]
home3 = [1, 1, 1, 0, 0]

listziphome = list(zip(home1, home2, home3))

print(listziphome)
