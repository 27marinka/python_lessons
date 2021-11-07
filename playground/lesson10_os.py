import os
from os import path
import sys

print(os.name)
print(os.getlogin())
print(os.getpid())
# print(os.environ)
# a = os.system("ls")
print(os.listdir("./.."))
print(os.getcwd())
print(os.chdir("../../"))
print(os.getcwd())

print("===========")

print(path.abspath("."))
print(path.abspath(__file__))

basepath = path.dirname(path.abspath(__file__))
print(basepath)
newfilepath = path.join(basepath, "NEW_DIR")
print(newfilepath)

print("==================")

for item in os.listdir():
    print(item, path.isdir(item), path.isfile(item),  path.islink(item))

print("==================")

print(sys.platform)
print(sys.maxsize)
print(sys.getrecursionlimit())
print(sys.argv)