
import numpy as np
import time
import sys
sys.setrecursionlimit(9999999)


def quicksort(a, p, r):
    if(p < r):
        q = partition(a, p, r)
        quicksort(a, p, q-1)
        quicksort(a, q+1, r)


def partition(a, p, r):
    x = a[r]
    i = p-1
    for j in range(p, r):
        if a[j] <= x:
            i = i+1
            h = a[i]
            a[i] = a[j]
            a[j] = h
    z = a[i+1]
    a[i+1] = a[r]
    a[r] = z
    return(i+1)
