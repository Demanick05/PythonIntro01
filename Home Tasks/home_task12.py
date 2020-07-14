"""
Given a list. Remove the number with the idex, which enters user and shift to the left all elements after the removed number.
"""

import random

lst = [random.randint(0, 100) for _ in range(10)]
print(lst)

k = int(input("Enter the index of element to delete: "))
lst.remove(lst[k])
print(lst)