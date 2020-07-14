"""
Given a list. Swap the number with given index to a number, which is entered by user
"""

import random

lst = [random.randint(0, 100) for _ in range(10)]
print(lst)

k = int(input("Enter the index of the object to swap: "))
c = int(input("Enter the number to insert on index K: "))

lst.append(0)
for i in range(len(lst)-1, k, -1):
    lst[i] = lst[i-1]

lst[k] = c
print(lst)