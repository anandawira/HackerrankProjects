#!/bin/python3

import sys
import math
 
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
                result = result +  (i + num/i);
        i = i + 1
         
    # Add 1 to the result as 1 is also
    # a divisor
    return int(result + 1);

limit = 10**5
ans_list = [0] * (limit + 1)

for a in range(1, limit+1):
    b = divSum(a)
    if a == b:
        continue
    d_b = divSum(b)
    
    if a == d_b:
        ans_list[a] = a
        
        if b <= limit:
            ans_list[b] = b
    
def solve(n):
    return sum(ans_list[:n+1])

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(solve(n))