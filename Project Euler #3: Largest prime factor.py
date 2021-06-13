#!/bin/python3

import sys
import math

def biggestPrimeDivisor(n):
    remain = n
    divisor = 3
    
    while remain%2==0:
        remain /= 2
        
    while remain!=1 and divisor<=math.sqrt(n):
        if remain%divisor == 0:
            remain /= divisor
        else:
            divisor += 2
            
    result = remain if remain != 1 else divisor
            
    print(int(result)) 


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    biggestPrimeDivisor(n)
