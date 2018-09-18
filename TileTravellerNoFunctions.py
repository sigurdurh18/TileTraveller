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
            possible="n"
        elif (cordY == 2):
            print("You can travel: (N)orth or (E)ast or (S)outh.")
            possible="nes"
        elif (cordY == 3):
            print("You can travel: (E)ast or (S)outh.")
            possible="es"
    if (cordX == 2):
        if (cordY == 1):
            print("You can travel: (N)orth.")
            possible="n"
        elif (cordY == 2):
            print("You can travel: (S)outh or (W)est.")
            possible="sw"
        elif (cordY == 3):
            print("You can travel: (E)ast or (W)est.")
            possible="ew"
    if (cordX == 3):
        if (cordY == 2):
            print("You can travel: (N)orth or (S)outh.")
            possible="ns"
        elif (cordY == 3):
            print("You can travel: (S)outh or (W)est")
            possible="sw"
    direction=input("Direction: ").lower()
    if(direction in possible) and len(direction)==1:
        if direction=='n' and cordY !=3:
            cordY+=1
        elif direction =='s' and cordY!=1:
            cordY-=1
        elif direction == 'e' and cordX != 3:
            cordX+=1
        elif direction == 'w' and cordX != 1:
            cordX-=1
        else:
            print("Not a valid direction!",cordX,cordY)
    else:
        print("Not a valid direction!",cordX,cordY)
print("Victory!")