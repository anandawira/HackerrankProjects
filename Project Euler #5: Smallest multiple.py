#!/bin/python3

import sys
import math

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // math.gcd(a, b)

def solve(n):
    current = 1
    for i in range(1, n+1):
        current = lcm(current, i)
    print(current)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    solve(n)
