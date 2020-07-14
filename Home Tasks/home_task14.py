"""
Given two lists. Count how many unique elements are in both of them.
"""

import random


#generating lists
lst1 = [random.randint(0, 50) for _ in range(10)]
lst2 = [random.randint(0, 50) for _ in range(10)]

#counting the amount of unique numbers
unique = len(set(lst1+lst2))
print(lst1, '\n', lst2, '\n', unique,)