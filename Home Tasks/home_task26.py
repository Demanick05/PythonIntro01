"""
Create file with the lines, which entered by user. Close file, if the line is empty
"""
fname = input('File: ')
f = open(fname,'w')
while True:
    s = input()
    if s == '': break
    f.write(s+'\n')
f.close()