#!/bin/python3

import sys

LIMIT = 10**5

def GenerateAnswer():
    
    #initialize scenario of only using 1p
    number_of_ways = [1]*(LIMIT+1)
    
    for coin in [2, 5, 10, 20, 50, 100, 200]:
        new_ways = [1]*(LIMIT+1)
        for i in range(1, LIMIT+1):
            if i<coin :
                new_ways[i] = number_of_ways[i]
            else:
                new_ways[i] = number_of_ways[i] + new_ways[i-coin]
        number_of_ways = new_ways

    return number_of_ways

answers = GenerateAnswer()

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(answers[n]%(10**9 + 7))