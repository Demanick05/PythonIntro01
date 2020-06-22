string = input("Type something: ")

print(string[1])  #only the second character
print(string[-2])  #the one before the last character
print(string[:5])  #all characters from the start up to 5th
print(string[:-3])  #all characters from the start up to the third one to the end
print(string[3::2])  #all even-index characters, considering that 0 isn't even number
print(string[1::2])  #all odd-index characters
print(string[::-1])  #all the string backwards
print(string[::-2])  #string backwasrds, skipping 1 character
print(len(string))  #string length
