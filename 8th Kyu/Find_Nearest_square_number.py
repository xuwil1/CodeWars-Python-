#Your task is to find the nearest square number, nearest_sq(n), of a positive integer n.

#Goodluck :)

import math 
def nearest_sq(n):
    root=math.sqrt(n);
    if root - math.floor(root) < 0.5:
        root = math.floor(root)
    else:
        root = math.ceil(root)
    return root*root
