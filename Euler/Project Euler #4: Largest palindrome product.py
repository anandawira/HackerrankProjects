#!/bin/python3

import sys
import math

def reverseNumber(num):
    n = num; 
    rev = 0
  
    while(n > 0): 
        a = n % 10
        rev = rev * 10 + a 
        n = n // 10
      
    return rev
  

def solve(n):
    thousand = n//1000
    nSqrtFloor = math.floor(math.sqrt(n))
    
    while True:
        currentPalindrome = thousand*1000 + reverseNumber(thousand)
        
        if currentPalindrome < n:
            for d in range(nSqrtFloor, 1, -1):
                if currentPalindrome%d == 0 :
                    if d<1000 and currentPalindrome/d<1000:
                        return currentPalindrome
        thousand -=1

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(solve(n))
