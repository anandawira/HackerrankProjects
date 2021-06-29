#!/bin/python3

import sys, itertools, math

n, k = [int(num) for num in input().strip().split(' ')]

m_candidates = list()
for i in range(1, math.ceil(math.log10(n))+1 ):
    ms = list(itertools.permutations(list(range(1,k+1)), r=i))
    m_candidates += ms

def convert(list):
      
    # Converting integer list to string list
    s = [str(i) for i in list]
      
    # Join list items using join()
    res = int("".join(s))
      
    return(res)

m_candidates = [convert(m) for m in m_candidates if convert(m)<n]
del m_candidates[0]

def IsPandigitalMultiplier(m, k):
    pan = ''
    for i in range(1, 10):
        cur = str(m*i)
        
        for d in cur:
            if d in pan:
                return False
            
        pan += cur
        
        if len(pan)<k:
            continue
        
        if len(pan)>k:
            return False
        
        # n == len(pan)
        
        for i in range(1, k+1):
            if not str(i) in pan:
                return False
            
        return True
    

for m in m_candidates:
    if IsPandigitalMultiplier(m, k):
        print(m)

# print(m_candidates)