#!/bin/python3

import sys

def IsPalindrome(num):
    num = str(num)
    if num == num[::-1]:
        return True
    else:
        return False

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(str(n % b))
        n //= b
    return ''.join(digits[::-1])

n, k = [int(num) for num in input().strip().split(' ')]

sum = 0
for i in range(1, n):
    if not IsPalindrome(i):
        continue
    
    if IsPalindrome(numberToBase(i, k)):
        sum+=i
        
print(sum)
    