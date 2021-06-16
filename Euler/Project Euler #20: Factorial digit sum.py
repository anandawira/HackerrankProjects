#!/bin/python3

import sys, math

def solve(n):
    number = math.factorial(n)
    text = str(number)
    result = sum([int(a) for a in text])
    return result

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(solve(n))