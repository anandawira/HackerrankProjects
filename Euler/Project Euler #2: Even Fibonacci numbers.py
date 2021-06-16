#!/bin/python3

import sys

def generateEvenFibbonaciArray(n):
    resultArray = []
    
    a = 0
    b = 1
    
    while True:
        temp = a+b
        a = b
        b = temp
        
        if b > n:
            break
        
        if b%2 == 0:
            resultArray.append(b)
            
    return resultArray

def solve(n):
    print(sum(generateEvenFibbonaciArray(n)))

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    solve(n)
