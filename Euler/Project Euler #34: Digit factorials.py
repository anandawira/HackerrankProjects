#!/bin/python3

import sys, math, functools

n = int(input().strip())

FACTORIALS = [math.factorial(i) for i in range(10)]

def IsCurious(num):
    nums = [int(a) for a in str(num)]
    sum = functools.reduce(lambda a, b: a+FACTORIALS[b], nums, 0)
    return sum%num == 0
    
answer = 0

for i in range(10, n):
    if IsCurious(i):
        answer+=i
print(answer)