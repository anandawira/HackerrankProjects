#!/bin/python3
import sys
import math

def solve(n, m):
    return math.factorial(n+m)//(math.factorial(n)*math.factorial(m)) % 1000000007


t = int(input().strip())
for a0 in range(t):
    n,m = input().strip().split(' ')
    n,m = [int(n), int(m)]
    print(solve(n, m))