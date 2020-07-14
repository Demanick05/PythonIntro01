"""
Create a function, which calculates perimeter, square and diagonal of a square based on its one side.
"""
import math

def square (a):
    perimeter = a*4
    sqr = a**2
    diagonal = round((math.sqrt(2)*a), 2) #in order to calculate the diagonal, had to import math module; also rounded it by two numbers after comma
    return perimeter, sqr, diagonal

side = int(input("Please, enter the value of square's side: "))

print(square(side))