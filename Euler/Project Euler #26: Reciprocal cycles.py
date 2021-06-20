#!/bin/python3

import sys

cache = [None] * (10**4+1)
def getDecimals(denom):
    if cache[denom] != None:
        return cache[denom]
    # Find the (n+1)th remainder after
    # decimal point in value of 1/n
    rem = 1 # Initialize remainder
    for i in range(1, denom + 2):
        rem = (10 * rem) % denom
 
    # Store (n+1)th remainder
    d = rem
     
    # Count the number of remainders
    # before next occurrence of
    # (n+1)'th remainder 'd'
    count = 0
    rem = (10 * rem) % denom
    count += 1
    while rem != d :
        rem = (10 * rem) % denom
        count += 1
    
    cache[denom] = count
    return count
  
def get_top(n):
    top = {'d': 0, 'val': 0}
    for d in range(3, n):
        cycle = getDecimals(d)
        if cycle>top['val']:
            top['d'] = d
            top['val'] = cycle
    return top['d']
# ans_list = [None] * (10**4+1)
# top = {'d': 0, 'value': 0}
# for n in range(4, 10**2+1):
#     d = n-1
#     cycle = getDecimals(d)
#     if cycle>top['value']:
#         top['d'] = d
#         top['value'] = cycle
#     ans_list[n] = top['d']
# print(ans_list[:30])
    
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(get_top(n))