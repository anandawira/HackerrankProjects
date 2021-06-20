#!/bin/python3

import sys, itertools, math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False
 
    max_div = math.floor(math.sqrt(n))
    for i in range(3, 1 + max_div, 2):
        if n % i == 0:
            return False
    return True
    
    
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
            
    return [i for i in range(2, n+1) if prime[i]]

def GenerateCombination(n):
    b_list = SieveOfEratosthenes(n)
    a_list = list(range(1, n+1))
    a_list += [num*-1 for num in a_list]
    
    coms = itertools.product(a_list, b_list)
    return coms

# prime_list = SieveOfEratosthenes(26000)
# def RemoveNonPrime(coms, x):
#     new_coms = []
#     for com in coms:
#         result = x**2 + com[0]*x + com[1]
#         if result in prime_list:
#             new_coms.append(com)
#     return new_coms

def RemoveNonPrime(coms, x):
    new_coms = []
    for com in coms:
        result = x**2 + com[0]*x + com[1]
        if is_prime(result):
            new_coms.append(com)
    return new_coms

def Solve(n):
    coms = GenerateCombination(n)
    
    counter = 1
    while True:
        coms = RemoveNonPrime(coms, counter)
        
        if len(coms) == 1:
            break
        
        counter += 1
        
    return coms[0][0], coms[0][1]


n = int(input().strip())
a, b = Solve(n)
print(a, b)