#!/bin/python3

import sys

def splitNum(num, n, k):
    nums = []
    for i in range(n-k+1):
        nums.append(num[i: i+k])
    return nums

def productNum(num):
    result = 1
    for i in range(len(num)):
        result *= int(num[i])
    return result

    
def solve(num, n, k):
    nums = splitNum(num, n, k)
    
    top = 0
    for num in nums:
        product = productNum(num)
        if product>top:
            top=product
            
    print(top)
    
t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    solve(num, n, k)