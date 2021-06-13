#!/bin/python3

import sys, math

def solve(n):
    top = -1
    for a in range(1, ((n-3)//3)+1 ):
        b = n*(n-2*a) // (2*(n-a))
        c = n-a-b
        
        if not (a<b and b<c):
            continue
        
        if not (a%1==0 and b%1==0):
            continue
        
        if not (a**2 + b**2 == c**2):
            continue
        
        if a*b*c > top:
            top = a*b*c

    return top

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(solve(n))