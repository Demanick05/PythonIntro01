"""
Create a function, which takes two integer arguments (numbers) and their operator as a third argument.
This function should return result of operation between these two numbers.
"""

def arithmetic (a, b, c):
    if  c == "+":
        return a+b
    elif c == "-":
        return  a-b
    elif c == "*":
        return a*b
    elif c == "/":
        return a/b
    else: return "Unknown operation!"

a = int(input("Please, enter the first number: "))
b = int(input("Please, enter the second number: "))
c = input("Please, select an operation to perform with the numbers: ")

print(arithmetic(a, b, c))