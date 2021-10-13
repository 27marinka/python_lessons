import time
import datetime
import random

date_my = "02.03.2021"

now = datetime.datetime.now()
print(now)

print(now.timestamp())

rand_var = random.randint(2, 7)
print(rand_var)

some_list = ["bob", "goo", "horror"]
print(random.choice(some_list))