from os import *
from sys import *
from collections import *
from math import *

def firstAndLastPosition(arr, n, k):

    # Write your code here
    f=first_occ(arr,n,k)
    l=last_occ(arr,n,k)
    
    return f,l


def first_occ(arr,n,key):
    s=0
    e=n-1
    m=(s+e)//2
    ans=-1
    while(s<=e):
        if key==arr[m]:
            ans=m
            e=m-1
        elif key>arr[m]:
            s=m+1
        else:
            e=m-1
        m=(s+e)//2
    return ans


def last_occ(arr,n,key):
    s=0
    e=n-1
    m=(s+e)//2
    ans=-1
    while(s<=e):
        if key==arr[m]:
            ans=m
            s=m+1
        elif key>arr[m]:
            s=m+1
        else:
            e=m-1
        m=(s+e)//2
    return ans
    