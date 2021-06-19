#!/bin/python3

import sys, functools

def getWordWorth(word):
    worth = functools.reduce(lambda a, b: a+ord(b)-64, word, 0)
    return worth

def getIndex(names, name):
    return names.index(name)+1


n = int(input().strip())
names = []
for _ in range(n):
    name = input().strip()
    names.append(name)
    
names.sort()

q = int(input().strip())
for _ in range(q):
    q = input().strip()
    worth = getWordWorth(q)
    idx = getIndex(names, q)
    print(worth*idx)