#!/bin/python3

import sys

LIMIT = 10**9 + 7

def GetSum(n):
    s = (n-1)//2
    
    return ((16*s**3 + 30*s**2 + 26*s +3)//3)%LIMIT

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(GetSum(n))