#!/bin/python3

import sys

def odd(n):
    return 3*n+1

def even(n):
    return n>>1

def memoize_collatz(f):
    memory = [0]*5000001
  
    # This inner function has access to memory
    # and 'f'
    def inner(n):
        if n<5000000:
            if memory[n] == 0:
                memory[n] = f(n)
            
            return memory[n]
        else:
            return f(n)
    return inner

@memoize_collatz
def collatz(n):
    if n != 1:
        if n%2 == 0:
            n = even(n)
        else:
            n = odd(n)
        
        return collatz(n) + 1
    else:
        return 0
  
ans_list = [0]
top = 0
idx = 1  

for i in range(1, 5000000+1):
    result = collatz(i)
    if result>=top:
        top = result
        idx = i
    ans_list.append(idx)
    
def solve(n):
    return ans_list[n]    


# def solve(n):
#     top = 0
#     idx = 1
    
#     for i in range(1, n+1):
#         result = collatz(i)
#         if result>= top:
#             top = result
#             idx = i
    
#     return idx

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(solve(n))