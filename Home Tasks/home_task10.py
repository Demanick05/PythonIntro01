my_string = input("Type in some string: ")

left_index = my_string.find("h")
right_index = my_string.rfind("h")  #found indexes of the first and last "h" characters; they will serve as a strting point to form a resulting string

result = my_string[:left_index + 1] + my_string.replace("h", "H") + my_string[right_index:]

print(result)