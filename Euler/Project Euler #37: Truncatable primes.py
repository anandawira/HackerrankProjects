#!/bin/python3

import sys, math, time


def SieveOfEratosthenes(n):
 
    # Create a boolean array
    # "prime[0..n]" and initialize
    #  all entries it as true.
    # A value in prime[i] will
    # finally be false if i is
    # Not a prime, else true.
    prime = [True] * (n+1)
    p = 2
    while (p * p <= n):
        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] == True):
 
            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
            
    return [i for i in range(2, n+1) if prime[i]]

n = int(input().strip())
# start = time.time()

primes = SieveOfEratosthenes(n-1)
primesStr = [str(prime) for prime in primes]

s = ['0', '2', '4', '6', '8', '5']
def IsTrunctablePrime(num):
    if num<10:
        return False
    
    numStr = str(num)
    
    for d in numStr[1:]:
        if d in s:
            return False
    
    for i in range(len(numStr)):
        # if int(numStr[i:]) not in primes:
        #     return False
        # if int(numStr[:i+1]) not in primes:
        #     return False
        if int(numStr[:i+1]) not in primes:
            return False
        if int(numStr[-i:]) not in primes:
            return False
        
        
        
        
    return True

answer = 0

for prime in primes:
    if IsTrunctablePrime(prime):
        answer += prime
    
print(answer)
# print(primes)
# print(time.time()-start)