#!/bin/python3

import sys
from bisect import bisect_left

MAX = 24000
 
# Create an array for memoization
f = [0] * MAX
 
# Returns n'th fuibonacci number using table f[]
def fib(n) :
    # Base cases
    if (n == 0) :
        return 0
    if (n == 1 or n == 2) :
        f[n] = 1
        return (f[n])
 
    # If fib(n) is already computed
    if (f[n]) :
        return f[n]
 
    if( n & 1) :
        k = (n + 1) // 2
    else :
        k = n // 2
 
    # Applying above formula [Note value n&1 is 1
    # if n is odd, else 0.
    if((n & 1) ) :
        f[n] = (fib(k) * fib(k) + fib(k-1) * fib(k-1))
    else :
        f[n] = (2*fib(k-1) + fib(k))*fib(k)
 
    return f[n]

def get_digit(n):
    num = fib(n)
    digit = len(str(num))
    return digit
        
digits = [get_digit(num) for num in list(range(MAX))]

def BinarySearch(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    else:
        return -1

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(BinarySearch(digits, n))