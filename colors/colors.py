def mixColors(*colors: tuple):
    res = [0, 0, 0]
    for color in colors:
        for index, param in enumerate(color):
            res[index] += param
    return tuple(res)


def subtractColors(*colors: tuple):
    if "DEBUG" in colors: 
        ind = colors.index("DEBUG")
        print("Found debugging notice in element", ind+1, "( index", ind, "), initializing debugger")
        actualcolors = colors[:ind] + colors[ind+1:]
        print("              [DEBUGGING STARTED]")
        print("Running on color group:", actualcolors, "\n")
        res = list(actualcolors[0])
        for color in actualcolors[2:]:
            if type(color)==tuple and len(color)==3:
                print("Color: ", color) # DEBUG
                for index, param in enumerate(color):
                    if type(param)==int:
                        print(f"Index {index} => {param}") # DEBUG
                        print(res[index], "-", param) # DEBUG
                        res[index] -= param
                        print("      Current result is", res) # DEBUG
                print("   ----------  ") # DEBUG
        print("              [ DEBUGGING ENDED WITH RESULT",tuple(res),"]")
        return tuple(res)

    else:
        res = list(colors[0])
        for color in colors[1:]:
            if type(color)==tuple and len(color)==3:
                for index, param in enumerate(color):
                    if type(param)==int:
                        print(type(param))
                        res[index] -= param
        return tuple(res)

RED =  (255,   0,    0 )
BLUE = ( 0,    0,   255)
LIME = ( 0,   255,   0 )           
WHITE = mixColors(RED, BLUE, LIME)
BLACK = subtractColors(WHITE, "DEBUG", RED, BLUE, LIME)
print(BLACK)

def generateColor():
    import random
    return tuple([random.randint(0,255) for i in range(3)])



#todo: hex/hsl etc. support
#debug for mixcolors
#averagecolor function

