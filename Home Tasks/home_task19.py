"""
Write a program, which gets a list of lists as an input.
This program should return tuples, consisting of order number and price for all items in the purchase.
If the price will be less than $100 - increase it by $10.
"""

some_list = [[34587, "Learning Python, Mark Lutz", 4, 40.95], [98762, "Programming Pyhon, Mark Lutz", 5, 56.80],
             [77226, "Head First Pythin, Paul Barry", 3, 32.95],
             [88112, "Einfuhrung in Python3, Bernd Klein", 3, 24.99]]

price = [i[2] * i[3] if i[2] * i[3] >= 100 else (i[2] * i[3]) + 10 for i in some_list]
print(price)
order_number = [i[0] for i in some_list]
print(order_number)

result = (list(map(lambda x, y: (f'Price = {x}', f'Order = {y}'), price, order_number)))
print(result)

for i in result:
    print(i, end="\n")
