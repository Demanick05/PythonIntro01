first_class = int(input("How many students in the 1st class: "))
second_class = int(input("How many students in the 2nd class: "))
third_class = int(input("How many students in the 3rd class: "))

if first_class % 2 == 0: #check if the number of students is even (divides by 2 without remainder)
    desks_first = first_class // 2
    print("For the first class we need to buy", desks_first, "desks")
else:     
    desks_first = (first_class / 2) + 0.5
    print("For the first class we need to buy", int(desks_first), "desks") #transforming float result into integer


if second_class % 2 == 0:
    desks_second = second_class // 2
    print("For the second class we need to buy", desks_second, "desks")
else:
    desks_second = (second_class / 2) + 0.5
    print("For the second class we need to buy", int(desks_second), "desks")


if third_class % 2 == 0:
    desks_third = third_class // 2
    print("For the third class we need to buy", desks_third, "desks")
else:
    desks_third = (third_class / 2) + 0.5
    print("For the third class we need to buy", int(desks_third), "desks")

print("Overall number of desks to buy is", int(desks_first + desks_second + desks_third))