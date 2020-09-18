# git clone https://github.com/rognvaldur20/tile_traveller.git

x = 1
y = 1
game_beaten = False
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
        print("You can travel: (S)outh or (W)est.")
    if x == 3 and y == 2:
        print("You can travel: (N)orth or (S)outh.")
    if x == 3 and y == 1:
        print("You can travel: (N)orth.")
    if x == 2 and y == 2:
        print("You can travel: (S)outh or (W)est.")
    if x == 2 and y == 1:
        print("You can travel: (N)orth.")

def east(x,y):
    if x == 3:
        print("Not a valid direction!")
        return(x,y)
    elif x == 1 and y == 1:
        print("Not a valid direction!")
        return(x,y)
    elif x == 2 and (y == 2 or y == 1): #changed the first y part to 2 instead of 3, as they can move east from 2,3 but not 2,2
        print("Not a valid direction!")
        return(x,y)
    else:
        x += 1
        return(x,y)

def south(x,y):
    if y == 1:
        print("Not a valid direction!")
        return(x,y)
    elif x == 2 and y == 3:
        print("Not a valid direction!")
        return(x,y)
    else:
        y -= 1
        return(x, y)

def north(x,y):
    if y >= 3:
        print("Not a valid direction!")
        return(x,y)
    elif x == 2 and y == 2:
        print("Not a valid direction!")
        return(x,y)
    else:
        y+= 1
        return(x, y)

def west(x,y):
    if x == 1:
        print("Not a valid direction!")
        return(x,y)
    elif x == 3 and (y == 2 or y == 1):
        print("Not a valid direction!")
        return(x,y)
    else:
        x -= 1
        return(x,y)
        

while game_beaten != True:
    possible_moves(x,y)
    user_input = str(input("Direction: "))
    if user_input.lower() == "e":
        x,y = east(x,y)
    elif user_input.lower() == "w":
        x,y = west(x,y)
    elif user_input.lower() == "n":
        x,y = north(x,y)
    elif user_input.lower() == "s":
        x,y = south(x,y)
    else:
        print("Not a valid direction!")
    if x == 3 and y == 1:
        game_beaten = True #not sure if this is bad practice or not -P
else:
    print("Victory!")
