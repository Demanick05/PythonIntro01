"""
Create a function, which reverses given list.
"""

# generating the list
from random import randint

lst = [randint(1, 100) for _ in range(15)]
print(lst)


def list_reverse(s):
    char = list(s)
    for i in range(len(s) // 2):
        tmp = char[i]
        char[i] = char[len(s) - i - 1]
        char[len(s) - i - 1] = tmp
    return ''.join(str(char))


print(list_reverse(lst))
