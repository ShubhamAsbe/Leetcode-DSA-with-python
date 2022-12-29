from os import *
from sys import *
from collections import *
from math import *

def findArrayIntersection(arr: list, n: int, brr: list, m: int):
    # Write your code here
    # Return a list containing all the common elements in arr and brr.
    intersect=[]
    i=0
    j=0
    while(i<n and j<m):
        if arr[i]==brr[j]:
            intersect.append(brr[j])
            i+=1
            j+=1
        elif arr[i]<brr[j]:
            i+=1
        else:
            j+=1

    return intersect
    pass
