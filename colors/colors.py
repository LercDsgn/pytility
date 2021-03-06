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
# closerTo  ( returns a color that is which other given color is closer to the first one)
# generate  ( returns a randomly generated color [with more chance for a base color/colors (r/g/b) - if given] and [in a range - if given])
# rgbToHex, rgbToHsl, hexToRgb, hexToHsl, hslToRgb, hslToHex, convert, toRgb, toHex, toHsl ( returns given color converted to another type )
# isValid   ( returns a boolean based on whether the given tuple is a valid color representation or not )
# getColor  ( returns a color from given tuple, list, dictionary, string, int, float etc.)
# contrast  ( retrurns a color that is the opposite of given color
# weightedMix ( returns a color that is mix of given colors, each color at given weight) // maybe add weightedSubtract too? or maybe merge randomMix with this?
# randomMix  // maybe rename randomWeightedMix? maybe merge with weightedMix? maybe make randomSubtract?
# getColorFromImage (img directory, x, y, origin="top left")
# getDarkness // white-black intensity


#                                   || --------------------------------- ||

# pytility.(colorname)  - a default color object.
# pytility.colors       - a default list of color objects.
# pytility.Colors       - the color class. 
# --- String Info Constants ---
# pytility.features    
# pytility.contributors 
# pytility.changelog
# pytility.guide
class ColorError(Exception):
    pass
class Color:
    def __init__(self, r, g, b):
        higher, lower = [(i, f"at index {j+1}", ["red","green","blue"][j]) for j,i in enumerate((r,g,b)) if i > 255],      [(i, f"at index {j+1}", ["red","green","blue"][j]) for j,i in enumerate((r,g,b)) if i < 0]
        higher1, lower1 = [", ".join((str(i), f"at index {j+1}", ["red","green","blue"][j])) for j,i in enumerate((r,g,b)) if i > 255],      [", ".join((str(i), f"at index {j+1}", ["red","green","blue"][j])) for j,i in enumerate((r,g,b)) if i < 0]
        if not (len(higher) or len(lower)):
            self.red = r
            self.green = g
            self.blue = b
            self.tupled = (r,g,b)
            self.dicted = { (["red", "green", "blue"][j], i) for j, i in enumerate((r,g,b))}
        else: 
            raise ColorError(f"Color object values must be between 0 and 255. Higher than 255: {higher1}, Lower than 0: {lower1}")

def capColor(color):
    if type(color)==Color: raise ColorError("Color to be capped must be type of Color class")
    return 255 if color > 255 else 0 if color < 0 else color



def colorFromTuple(source):
  return Color(*source)
    
def cappedMix(*colors: Color) -> Color:
    print (len(colors))
    """Mix given amount of colors."""
    """
    res = [0]*3
    for color in colors:
        for index, param in enumerate(color):   
            if 0 > res[index]+param > 255: 
                res[index] += param
    """
    col = lambda x: sum([eval(f"color.{x}") for color in colors])
    r,g,b = col("red"), col("green"), col("blue")
   
    return Color(*map(capColor, (r,g,b)))

def mix(*colors: Color) -> Color:
    """Mix given amount of colors."""
    """
    res = [0]*3
    for color in colors:
        for index, param in enumerate(color):   
            if 0 > res[index]+param > 255: 
                res[index] += param
    """
    col = lambda x: sum([eval(f"color.{x}") for color in colors])
    r,g,b = col("red"), col("green"), col("blue")
   
    try: 
        return Color(r,g,b)
    except ColorError:
        raise ColorError("The values of the mix of colors must be between 0 and 255")
        


def subtract(*colors: Color) -> Color:
    """ Return a color by subtracting all other given colors from the first one """
    res = list(colors[0])
    for color in colors[1:]:
        if type(color) == tuple and len(color) == 3:
            for index, param in enumerate(color):
                if type(param) == int and 0 < res[index] < 255:
                    res[index] -= param
    return colorFromTuple(res)



def generateColor():
    import random
    return tuple([random.randint(0, 255) for i in range(3)])

# EXAMPLE
# r,g,b = (255,0,0), (0,255,0), (0,0,255)
# subract(mix(r,g,b),r,g,b) # (0,0,0)



a = Color(255, 0, 0)
b = Color(1, 0, 255)
z = cappedMix(a,b)
print(z.tupled)
