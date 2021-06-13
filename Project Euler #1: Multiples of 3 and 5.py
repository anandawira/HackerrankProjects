#!/bin/python3

import sys
import math

def sumOfMultiple(n, multiple):
    n=n-1
    if n<multiple:
        return 0
    
    max = n//multiple
    return math.floor((((max*max) + max)//2)*multiple) 

def solve(n):
    sumOf3 = sumOfMultiple(n, 3)
    sumOf5 = sumOfMultiple(n, 5)
    sumOf15 = sumOfMultiple(n,15)
    
    return sumOf3 + sumOf5 - sumOf15

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(solve(n))
    