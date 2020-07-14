"""
Create a function, which calculates whether the year is leap or not.
"""


def year_is_leap (a): #the year is leap if it can be evenly divided by 4
    if a%4 == 0:
        return "This year is leap!"
    else:
        return "This year is NOT leap!"

year = int(input("Please, enter the year: "))
print(year_is_leap(year))