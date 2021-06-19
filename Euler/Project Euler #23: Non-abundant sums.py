#!/bin/python3

import sys, math, itertools

# Returns sum of all factors of n.
def divSum(num) :
     
    # Final result of summation of divisors
    result = 0
     
    # find all divisors which divides 'num'
    i = 2
    while i<= (math.sqrt(num)) :
       
        # if 'i' is divisor of 'num'
        if (num % i == 0) :
       
            # if both divisors are same then
            # add it only once else add both
            if (i == (num / i)) :
                result = result + i;
            else :
                result = result +  (i + num//i);
        i = i + 1
         
    # Add 1 to the result as 1 is also
    # a divisor
    return result + 1

limit = 10**5
min_abudant = 12
max_non_abudant = 28123

ans_list = [False]*(max_non_abudant+1) + [True]*(limit-max_non_abudant)

abudants = []
for num in range(min_abudant, max_non_abudant-min_abudant+1):
    if divSum(num)>num:
        abudants.append(num)
    
for a in abudants:
    for b in abudants:
        idx = a+b
        ans_list[idx] = True


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print('YES' if ans_list[n] else 'NO')