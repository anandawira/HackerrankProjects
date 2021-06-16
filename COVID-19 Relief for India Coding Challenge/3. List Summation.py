#!/bin/python3

import sys

def solve(a, b):
    sumA = sum(a)
    sumB = sum(b)
    
    zeroA = a.count(0)
    zeroB = b.count(0)
    
    totalA = sumA+zeroA
    totalB = sumB+zeroB
    
    if zeroA == 0:
        if totalA < totalB:
            return -1
        
    if zeroB == 0:
        if totalB < totalA:
            return -1
    
    return max(totalA, totalB)

listA = []
listB = []

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    listA.append(n)
    
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    listB.append(n)
    
print(solve(listA, listB))