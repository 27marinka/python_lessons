word = 'abcdefg'
word_len = len(word)
print("length is: " + str(word_len))
for i in range(word_len - 1, -1, -1):
    print(i)

listik_my = [1, 2, 3]


def mult(listik):
    map(
        lambda x: x*2,
        listik
    )

mult(listik_my)

