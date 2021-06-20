#!/bin/python3

import sys

def Solve(n):
    return sum([i for i in range(10**2, 10**6) if i == sum(int(a)**n for a in str(i))])
    
        

n = int(input().strip())
print(Solve(n))