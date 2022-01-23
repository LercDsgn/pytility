def mix(*colors: tuple) -> tuple:
    """Mix given amount of colors."""
    res = [0]*3
    for color in colors:
        for index, param in enumerate(color):   
            if 0 > res[index]+param > 255: 
                res[index] += param
    return tuple(res)



def subtract(*colors: tuple) -> tuple:
    """Subtract given amount of colors."""
    res = list(colors[0])
    for color in colors[1:]:
        if type(color) == tuple and len(color) == 3:
            for index, param in enumerate(color):
                if type(param) == int and 0 < res[index] < 255:
                    res[index] -= param
    return tuple(res)



def generateColor():
    import random
    return tuple([random.randint(0, 255) for i in range(3)])

# EXAMPLE
# r,g,b = (255,0,0), (0,255,0), (0,0,255)
# subract(mix(r,g,b),r,g,b) # (0,0,0)



