#!/bin/python3

import sys, math

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']

def getFac(num, digits):
    num -= 1
    fac = [0]*digits
    
    for i in range(digits):
        fac[i] = num//math.factorial(digits-1-i)
        num %= math.factorial(digits-1-i)
        
    return fac

def fac_to_permutation(fac, letters):
    result = ''
    for i in range(len(letters)):
        result += letters.pop(fac[i])
        
    return result

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    fac = getFac(n, 13)
    perm = fac_to_permutation(fac, letters.copy())
    print(perm)