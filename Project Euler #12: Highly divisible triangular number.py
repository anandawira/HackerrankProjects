#!/bin/python3

import sys, math

def f(L, nMax=45000):
    d = [0]*nMax
    for n in range(1, nMax):
        for j in range(n, nMax, n):
            d[j]+= 1
        nDiv = d[n-1]*d[n//2] if n%2==0 else d[(n-1)//2]*d[n]
        if nDiv > L: return (n-1)*n//2

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(f(n))