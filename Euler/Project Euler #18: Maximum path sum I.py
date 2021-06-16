#!/bin/python3

import sys

cached_comb = [0]*(15+1)

def generateCombination(n):
    if cached_comb[n] != 0:
        return cached_comb[n]
    
    result = []
    if n==1:
        result = [[0],]
    else:
        for com in generateCombination(n-1):
            last = com[-1]
            result.append(com + [last] )        
            result.append(com + [last+1] )
    
    cached_comb[n] = result
    return result

def selectMaximum(numbers, combinations):
    top = 0
    for combination in combinations:
        sum = 0
        for i in range(len(numbers)):
            sum += numbers[i][combination[i]]
        
        if sum>top:
            top = sum
            
    return top


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    nums = []
    for a1 in range(n):
        row = [int(num) for num in input().strip().split(' ')]
        nums.append(row)
        
    coms = generateCombination(n)
    top = selectMaximum(nums, coms)
    print(top)
