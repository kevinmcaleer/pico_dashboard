import math
def rgb2hsv(r:int, g:int, b:int):
    """ Converts an RGB colour to HSV """
    h = 0
    s = 0
    v = 0
    # constrain the values to the range 0 to 1
    r_normal, g_normal, b_normal,  = r / 255, g / 255, b / 255
    cmax = max(r_normal, g_normal, b_normal)
    cmin = min(r_normal, g_normal, b_normal)
    delta = cmax - cmin
    
    # Hue calculation
    if(delta ==0):
        h = 0
    elif (cmax == r_normal):
        h = (60 * (((g_normal - b_normal) / delta) % 6))
    elif (cmax == g_normal):
        h = (60 * (((b_normal - r_normal) / delta) + 2))
    elif (cmax == b_normal):
        h = (60 * (((r_normal - g_normal) / delta) + 4))
    
    # Saturation calculation
    if cmax== 0:
        s = 0
    else:
        s = delta / cmax
        
    # Value calculation
    v = cmax
    
    colour = {'hue':h,'sat':s,'val':v}
    
    return colour     

def hsv2rgb(hue, sat, val):
    """ Sets the Hue Saturation and Value of the indexed RGB LED"""

    i = math.floor(hue * 6)
    f = hue * 6 - i
    p = val * (1 - sat)
    q = val * (1 - f * sat)
    t = val * (1 - (1 - f) * sat)

    r, g, b = [
        (val, t, p),
        (q, val, p),
        (p, val, t),
        (p, q, val),
        (t, p, val),
        (val, p, q),
    ][int(i % 6)]
    r = int(r*255)
    g = int(g*255)
    b = int(b*255)
    
    colour = {'red':r, 'green': g, 'blue':b}
    
    return colour

def mix(rgb1, rgb2):
    """ Mixes two RGB colours """
    r = (rgb1['red'] + rgb2['red']) / 2
    g = (rgb1['green'] + rgb2['green']) / 2
    b = (rgb1['blue'] + rgb2['blue']) / 2
    return {'red':r, 'green': g, 'blue':b}

def fade(rgb1, rgb2, amount:float):
    """ Fades between two RGB colours """
    r = int((rgb1['red'] * (1 - amount) + rgb2['red'] * amount))
    g = int((rgb1['green'] * (1 - amount) + rgb2['green'] * amount))
    b = int((rgb1['blue'] * (1 - amount) + rgb2['blue'] * amount))
    return {'red':r, 'green': g, 'blue':b}