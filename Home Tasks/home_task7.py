horse_x = int(input("Please, enter horse's X point: "))
horse_y = int(input("Please, enter horse's Y piint: "))

move_x = int(input("Please, enter needed X point: "))
move_y = int(input("Please, enter needed Y point: "))

if abs(horse_x - move_x) == 2 and abs(horse_y - move_y) == 1: #using "abs" function to eliminate the negative difference and get the
    print("Horse can move to that point")
elif abs(horse_x - move_x) == 1 and abs(horse_y - move_y) == 2:
    print("Horse can move to that point")
else:
    print("Horse CAN NOT move to that point!")