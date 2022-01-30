"""
                                                Pytility v0.01a
                                          Color Functions Demonstration
                                                January 30, 2021 
"""
#                                           [ CURRENT FUNCTIONS ]
#                                  || --------------------------------- ||
# mix       ( returns a color sum of given colors )
# onlyEmpty ( returns a color with only given position or r/g/b empty (0), all others are full (255) by default or given value )
# onlyFill  ( returns a color with only given position or r/g/b full (255) by default or given value, all others are empty (0) )
# all       ( returns a color with all positions (r/g/b) the same given value ) 
# reduce    ( returns a color all other given colors subtracted from the first one )
# blend     ( returns a color arithmetic mean of given colors )
# closerTo  ( returns which other given color is closer to the first one)
# generate  ( returns a randomly generated color [with more chance for a base color/colors (r/g/b) - if given] and [in a range - if given])
# rgbToHex, rgbToHsl, hexToRgb, hexToHsl, hslToRgb, hslToHex, convert, toRgb, toHex, toHsl ( returns given color converted to another type )
# isValid   ( returns a boolean based on whether the given tuple is a valid color representation or not )
# getColor  ( returns a color from given tuple, list, dictionary, string, int, float etc.)
#                                   || --------------------------------- ||

# pytility.(colorname)  - a default color object.
# pytility.colors       - a default list of color objects.
# pytility.Colors       - the color class. 
# --- String Info Constants ---
# pytility.features    
# pytility.contributors 
# pytility.changelog
# pytility.guide

class Color:
    pass
def mix(*colors: Color) -> Color:
    """Mix given amount of colors."""
    res = [0]*3
    for color in colors:
        for index, param in enumerate(color):   
            if 0 > res[index]+param > 255: 
                res[index] += param
    return tuple(res)



def subtract(*colors: Color) -> Color:
    """ Return a color by subtracting all other given colors from the first one """
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



