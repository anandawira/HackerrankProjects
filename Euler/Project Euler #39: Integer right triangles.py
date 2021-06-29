#!/bin/python3

import sys, time, math, bisect

# start = time.time()
def GenerateTriple(m, n):
    return 2*m*(m+n)

def GetMaxN(m):
    return (MAX_P - 2*m**2) // (2*m)

MAX_P = 5 * 10**6
MAX_M = 1580
freq = [0] * (MAX_P + 1)

for m in range(2, MAX_M+1):
    for n in range(1, m):
        if not math.gcd(m, n) == 1:
            continue
        
        if (m+n)%2==0:
            continue
        
        p = GenerateTriple(m, n)
        
        for k in range(1, MAX_P//p+1):
            freq[p*k] += 1
            
answers = [0]*(MAX_P+1)

top_idx = 0
top_f = 0
for idx, f in enumerate(freq):
    if f>top_f:
        top_f = f
        top_idx = idx
    answers[idx] = top_idx
              
def Solve(n):
    return answers[n]
# # print(freq)
# # print(time.time()-start)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(Solve(n))