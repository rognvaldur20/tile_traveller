print("Pálína var hérna")
print("Pálína var hérna aftur")



x = 1
y = 1
def possible_moves(x,y):
    if x ==  1 and y == 1:
        print ("You can move east and south")
    #gera fyrir alla reitina?

def east(x,y):
    if x == 3:
        print("invalid")
    elif x == 1 and y == 1:
        print("invalid")
    elif x == 2 and (y == 3 or y == 1):
        print("invalid")
    else:
        x += 1
        return(x,y)

def south(x,y):
    pass

def north(x,y):
    pass

def west(x,y):
    pass

while (x != 3) and (y != 1):
    possible_moves(x,y)
    user_input = input("where u wanna go?")
    if user_input == "e" or user_input == "E":
        x = east(x,y)
        #o.s.frv

print("Victory")