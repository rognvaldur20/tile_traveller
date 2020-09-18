# git clone https://github.com/rognvaldur20/tile_traveller.git

x = 1
y = 1
def possible_moves(x,y):

    if x ==  1 and y == 1:
        print ("You can travel: (N)orth.")
    if x == 1 and y == 2:
        print("You can travel: (N)orth or (E)ast or (S)outh.")
    if x == 1 and y == 3:
        print("You can travel: (E)ast or (S)outh.")
    if x == 2 and y == 3:
        print("You can travel: (E)ast or (W)est.")
    if x == 3 and y == 3:
        print("You can travel: (W)est or (S)outh.")
    if x == 3 and y == 2:
        print("You can travel: (N)orth or (S)outh.")
    if x == 3 and y == 1:
        print("You can travel: (N)orth.")
    if x == 2 and y == 2:
        print("You can travel: (W)est or (S)outh.")
    if x == 2 and y == 1:
        print("You can travel: (N)orth.")
    #gera fyrir alla reitina?

def east(x,y):
    if x == 3:
        print("Not a valid direction!")
    elif x == 1 and y == 1:
        print("Not a valid direction!")
    elif x == 2 and (y == 2 or y == 1): #changed the first y part to 2 instead of 3, as they can move east from 2,3 but not 2,2
        print("Not a valid direction!")
    else:
        x += 1
        return(x,y)

def south(x,y):
    if y == 1:
        print("Not a valid direction!")
    if x == 2 and y == 3:
        print("Not a valid direction!")
    else:
        y -= 1
        return(x, y)

def north(x,y):
    if y == 3:
        print("Not a valid direction!")
    if x == 2 and y == 2:
        print("Not a valid direction!")
    else:
        y+= 1
        return(x, y)

def west(x,y):
    if x == 1:
        print("Not a valid direction!")
    if x == 3 and (y == 2 or y == 1):
        print("Not a valid direction!")

while (x != 3) and (y != 1):
    possible_moves(x,y)
    user_input = input("Direction: ")
    if user_input.lower() == "e":
        east(x,y)
    if user_input.lower() == "w":
        west(x,y)
    if user_input.lower() == "n":
        north(x,y)
    if user_input.lower() == "s":
        south(x,y)
    else:
        print("Not a valid direction!")

print("Victory!")
