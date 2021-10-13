"""
1 Даны кортеж пользователей users и набор шаблонов templates
Задача обращаясь по индексу к кортежу пользователей напечатать на экране сообщение
если пользователю менее 7 лет: "{name} {surname} закончил школу"
Внимание конструкцию IF ELSE мы не используем (мы ее еще не изучали, и даже если знаете не используйте)
"""

users = (
    {
        "name": "Jon",
        "surname": "Smith",
        "age": 6,
    },
    {
        "name": "Bill",
        "surname": "Suns",
        "age": 20,
    }
)

templates = (
    "{name} {surname} закончил школу",
    "{name} {surname} скоро пойдет в школу",
)

template_dict = {False: templates[0], True: templates[1]}

user1 = users[0]
res1 = template_dict[user1["age"] < 7].format(name=user1["name"], surname=user1["surname"])
print(res1)
user2 = users[1]
res2 = template_dict[user2["age"] < 7].format(name=user2["name"], surname=user2["surname"])
print(res2)

"""
res1 = templates[1].format(name=users[0].get("name"), surname=users[0].get("surname"))
res2 = templates[0].format(name=users[1].get("name"), surname=users[1].get("surname"))

print(res1)
print(res2)
"""
