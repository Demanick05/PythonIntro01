my_number = int(input('Please, enter the number to reverse: '))

if my_number % 100 == 0: #check if the number ends with 0; otherwise the cycle won't calculate it the right way
    a = my_number // my_number - 1
else:
    a = my_number % 10

if my_number % 10 == 0: #check if the number contains 0 in the middle
    b = my_number // my_number - 1
else:
    b = my_number // 10 % 10

c = my_number // 100

if a == 0 and b == 0:
    res = (str(a * 100) + str(b * 10) + str(c)) #if the reversed number starts with 0, we need to transform it into string in order to see 0; otherwise integer will ignore 0 at the start
    print(res)
else:
    res = (a * 100) + (b * 10) + c
    print (res)