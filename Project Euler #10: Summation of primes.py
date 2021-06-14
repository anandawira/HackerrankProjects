#!/bin/python3

import sys

def SieveOfEratosthenes(n):
 
    # Create a boolean array
    # "prime[0..n]" and initialize
    #  all entries it as true.
    # A value in prime[i] will
    # finally be false if i is
    # Not a prime, else true.
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
 
        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] == True):
 
            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    
    prime[0] = prime[1] = False
    
    return prime

limit = 1000001

primes = SieveOfEratosthenes(limit)

sumPrimes = [0]*(limit+1)

top=0
for idx, val in enumerate(primes):
    if val:
        top += idx
    sumPrimes[idx] = top
    

def solve(n):
    print(sumPrimes[n])

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    solve(n)