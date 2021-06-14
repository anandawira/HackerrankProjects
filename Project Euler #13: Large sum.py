#!/bin/python3

import sys

sum = 0
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    sum += n
    
print(str(sum)[:10])