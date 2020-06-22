my_number = int(input("Please, enter the number: "))

i = 0
res = 0
while res < my_number:
    res **= i
    i += 1
    if res > my_number:
        print (my_number, i - 1, res, sep=" -> ")
else:
    print (my_number, i - 1, res, sep=" -> ")