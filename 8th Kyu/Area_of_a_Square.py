#Complete the function that calculates the area of the red square, when the length of the circular arc A is given as the input. Return the result rounded to two decimals.

from math import pi 
def square_area(A):  
    return round((A*2/pi)**2,2)
