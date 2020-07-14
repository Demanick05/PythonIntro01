"""
Create a function, which returns what season it is based on the month's number entered bu user
"""

def season (a):
    if a == 12 or a == 1 or a == 2:
        return "It's winter!"
    elif a > 2 and a <= 5:
        return "It's spring!"
    elif a > 5 and a <= 8:
        return  "It's summer!"
    elif a > 8 and a <= 11:
        return  "It's autumn!"
    else: return "Wrong month's number!"

month = int(input("Please, enter the number of month: "))

print(season(month))