"""
Given the number. Convert it to the other measuring system.
"""
number = int(input("Please, enter the number to convert: "))

#Creating converter as a function
def converter (n):
    s = ''
    while n > 0:
        s = str(n % 2) + s
        n //= 2
    return s

print(converter(number))
