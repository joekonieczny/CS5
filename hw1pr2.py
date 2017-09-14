# CS5 Gold, Lab1 part 2
# Filename: hw1pr2.py
# Name: Joe Konieczny
# Problem description: First few functions!


def dbl(x):
    """  output: dbl returns twice its input
         input x: a number (int or float)
         Spam is great, and dbl("spam") is better!
    """
    return 2*x

def tpl(x):
    """ output: tpl returns thrice its input
         input x: a number (int or float)
    """
    return 3*x

def sq(x):
    """ output sq returns the input, squared
    """
    
    return x*x

def interp(low,hi,fraction):
    """ output takes in three numbers, low, hi, and fraction, 
    and should return the floating-point value that is fraction 
    of the way between low and hi.
    """
    difference = hi - low
    stage2 = difference*fraction

    return stage2+low

def checkends(s):
    """ Checks the beginning and end of string 's' and returns
    'true' if the values match, false if not
    """

    if s[0] == s[-1]:
        return True
    else:
        return False

def flipsides(s):
    """ inputs string 's', then reverses the two halves of the string,
    for example "computer" would become "utercomp"
    """
    x = len(s)//2
    return s[-x:] + s[0:x+1]

def convertFromSeconds(s):
    """takes input 's' which is a # of seconds and returns the hours, minutes, and days of that value
    """
    days = s // (24*60*60)
    s = s % (24*60*60)
    hours = s // (60*60)
    s = s % (60*60)
    minutes = s // (60)
    s = s % (60)
    seconds = s
    return [days, hours, minutes, seconds]