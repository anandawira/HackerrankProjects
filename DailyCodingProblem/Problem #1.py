# This problem was recently asked by Google.

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?


#!/bin/python3

import sys, itertools

def Solve(n, k):
    sums = [sum(com) for com in itertools.combinations(n, r=2)]
    if k in sums:
        return True
    else:
        return False

n = [int(num) for num in input('Enter numbers separated by single space : ').strip().split(' ')]
k = int(input('Enter k : ').strip())

Solve(n, k)