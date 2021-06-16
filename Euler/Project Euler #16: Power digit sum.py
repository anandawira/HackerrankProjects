#!/bin/python3

import sys, math

def solve(n):
    try:
        num = int(math.pow(2, n))
    except:
        thousand = n//1000
        remains = n%1000
        num = 1
        for i in range(thousand):
            num *= int(math.pow(2, 1000))
        num *= int(math.pow(2, remains))
        
    txt = str(num)
    
    sum = 0
    for chr in txt:
        sum += int(chr)
        
    print(sum)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    solve(n)