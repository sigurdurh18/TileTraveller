'''
1: second version is easyer because it does not get as easaly cluttered
2: second version is mroe readable because it's not as cluttered
3: none
'''

def l11():
    print("You can travel: (N)orth.")
    direction = input("Direction: ").lower()
    if direction == 'n' and cordY != 3:
        return l12
    else:
        print("Not a valid direction!")
    return l11

def l12():
    print("You can travel: (N)orth or (E)ast or (S)outh.")
    direction = input("Direction: ").lower()
    if direction == 'n' and cordY != 3:
        return l13
    elif direction == 's' and cordY != 1:
        return l11
    elif direction == 'e' and cordX != 3:
        return l22
    else:
        print("Not a valid direction!")
    return l12

def l13():
    print("You can travel: (E)ast or (S)outh.")
    direction=input("Direction: ").lower()
    if direction =='s' and cordY!=1:
        return l12
    elif direction == 'e' and cordX != 3:
        return l23
    else:
        print("Not a valid direction!")
    return l13

def l21():
    print("You can travel: (N)orth.")
    direction=input("Direction: ").lower()
    if direction=='n' and cordY !=3:
        return l22
    else:
        print("Not a valid direction!")
    return l21

def l22():
    print("You can travel: (S)outh or (W)est.")
    direction = input("Direction: ").lower()
    if direction == 's' and cordY != 1:
        return l21
    elif direction == 'w' and cordX != 1:
        return l12
    else:
        print("Not a valid direction!")
    return l22

def l23():
    print("You can travel: (E)ast or (W)est.")
    direction = input("Direction: ").lower()
    if direction == 'e' and cordX != 3:
        return l33
    elif direction == 'w' and cordX != 1:
        return l13
    else:
        print("Not a valid direction!")
    return l23

def l32():
    print("You can travel: (N)orth or (S)outh.")
    direction = input("Direction: ").lower()
    if direction == 'n' and cordY != 3:
        return l33
    elif direction == 's' and cordY != 1:
        return l31
    else:
        print("Not a valid direction!")
    return l32

def l33():
    print("You can travel: (S)outh or (W)est")
    direction = input("Direction: ").lower()
    if direction == 's' and cordY != 1:
        return l32
    elif direction == 'w' and cordX != 1:
        return l23
    else:
        print("Not a valid direction!")
    return l33

def l31():
    print("Victory")
    return False

fun = l11
while fun:
    fun=fun()