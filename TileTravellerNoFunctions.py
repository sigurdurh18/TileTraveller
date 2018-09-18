'''
cordX = 1
cordY = 1
while cordX !=3 or cordY!=1:
    check traveling possibilitys
    print out posibilitys
    try to move based on input
        else don't move and print "Not a valid direction!"
'''

cordX=1
cordY=1
possible="n"

while cordX != 3 or cordY != 1:
    if (cordX == 1):
        if (cordY == 1):
            print("You can travel: (N)orth.")
            direction = input("Direction: ").lower()
            if direction == 'n' and cordY != 3:
                cordY += 1
            else:
                print("Not a valid direction!")

        elif (cordY == 2):
            print("You can travel: (N)orth or (E)ast or (S)outh.")
            direction = input("Direction: ").lower()
            if direction == 'n' and cordY != 3:
                cordY += 1
            elif direction == 's' and cordY != 1:
                cordY -= 1
            elif direction == 'e' and cordX != 3:
                cordX += 1
            else:
                print("Not a valid direction!")

        elif (cordY == 3):
            print("You can travel: (E)ast or (S)outh.")
            direction=input("Direction: ").lower()
            if direction =='s' and cordY!=1:
                cordY-=1
            elif direction == 'e' and cordX != 3:
                cordX+=1
            else:
                print("Not a valid direction!")

    if (cordX == 2):
        if (cordY == 1):
            print("You can travel: (N)orth.")
            direction=input("Direction: ").lower()
            if direction=='n' and cordY !=3:
                cordY+=1
            else:
                print("Not a valid direction!")
        elif (cordY == 2):
            print("You can travel: (S)outh or (W)est.")

            direction = input("Direction: ").lower()
            if direction == 's' and cordY != 1:
                cordY -= 1
            elif direction == 'w' and cordX != 1:
                cordX -= 1
            else:
                print("Not a valid direction!")

        elif (cordY == 3):
            print("You can travel: (E)ast or (W)est.")
            direction = input("Direction: ").lower()
            if direction == 'e' and cordX != 3:
                cordX += 1
            elif direction == 'w' and cordX != 1:
                cordX -= 1
            else:
                print("Not a valid direction!")
    if (cordX == 3):
        if (cordY == 2):
            print("You can travel: (N)orth or (S)outh.")

            direction = input("Direction: ").lower()
            if direction == 'n' and cordY != 3:
                cordY += 1
            elif direction == 's' and cordY != 1:
                cordY -= 1
            else:
                print("Not a valid direction!")
        elif (cordY == 3):
            print("You can travel: (S)outh or (W)est")
            direction = input("Direction: ").lower()
            if direction == 's' and cordY != 1:
                cordY -= 1

            elif direction == 'w' and cordX != 1:
                cordX -= 1
            else:
                print("Not a valid direction!")


print("Victory!")