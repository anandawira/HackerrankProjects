#!/bin/python3

import string
import sys
from string import ascii_lowercase
import itertools

def getDuplicateChar(s):
    chars = [c for c in string.ascii_lowercase if s.count(c)>1]
    duplicates = {}
    for char in chars:
        duplicates[char] = [idx for idx, val in enumerate(s) if val == char]
    return duplicates
    
def getShortestSubstring(s):
    duplicates = getDuplicateChar(s)
    if len(duplicates) == 0:
        return 0
    
    shortest = len(s)
    for isFirsts in itertools.product([True, False], repeat=len(duplicates)):
        vals = []
        for idx, val in enumerate(duplicates.values()):
            if isFirsts[idx]:
                vals += val[1:]
            else:
                vals += val[:-1]
        
        substringLength = max(vals) - min(vals) + 1
        if substringLength<shortest:
            shortest = substringLength
    return shortest
    

s = input().strip()
print(getShortestSubstring(s))