#!/bin/python3

import sys, collections, math

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

def isPrime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num%i == 0:
            return False
        
    return True

def convert(list):
      
    # Converting integer list to string list
    s = [str(i) for i in list]
      
    # Join list items using join()
    res = int("".join(s))
      
    return(res)

def GetRotatedNumbers(num):
    num = str(num)
    return [int(num[i:] + num[:i]) for i in range(len(num))]

n = int(input().strip())

s = ['0', '2', '4', '6', '8', '5']
def IsCircularPrime(prime):
    if prime<10:
        return True
    
    prime = str(prime)
    
    for i in s:
        if i in prime:
            return False
        
    for num in GetRotatedNumbers(prime):
        if not isPrime(num):
            return False
        
    return True
        

primes = SieveOfEratosthenes(n-1)

circularPrimes = [prime for prime in primes if IsCircularPrime(prime)]

print(sum(circularPrimes))
