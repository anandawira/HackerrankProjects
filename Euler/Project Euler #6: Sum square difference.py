#!/bin/python3

import sys
import math

def arithmeticSeries(n):
    return (n**2+n)/2

def kPerfectSum(k):
    return k*(k+1)*(2*k+1)/6

def solve(n):
    squareOfSum = arithmeticSeries(n)**2
    sumOfSquare = kPerfectSum(n)
    result = squareOfSum - sumOfSquare
    print(math.floor(result))

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    solve(n)