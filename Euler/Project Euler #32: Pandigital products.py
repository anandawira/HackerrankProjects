#!/bin/python3

import sys, itertools

def factor(num):
    return [(i, num // i) for i in range(1, int(num**0.5)+1) if num % i == 0]

def GetProducts(n):
    return [''.join(list(map(str, num))) for num in itertools.permutations(range(1,10), r=n)]

def IsPandigital(numStr, n):
    if len(numStr) != n:
        return False
    
    for i in range(1, n+1):
        if str(i) not in numStr:
            return False
        
    return True
    
    

def Solve(n):
    sum_pandigital = 0
    products = list()
    
    for i in range(1, (n//2)+1):
        products += GetProducts(i)
    
    for product in products:
        number = int(product)
        factor_pairs = factor(number)
        
        for pair in factor_pairs:
            pairStr = str(pair[0]) + str(pair[1])
            
            if IsPandigital(product+pairStr, n):
                sum_pandigital += int(product)
                break
    return sum_pandigital
# print(Solve(4))

# print(IsPandigital('159372684', 9))

n = int(input().strip())
print(Solve(n))