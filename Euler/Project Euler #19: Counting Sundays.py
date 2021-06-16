#!/bin/python3

import sys
from datetime import date

def switch(h) :
    return {
        0 : "Saturday",
        1 : "Sunday",
        2 : "Monday",
        3 : "Tuesday",
        4 : "Wednesday",
        5 : "Thursday",
        6 : "Friday",
    }[h]
 
def Zellercongruence(day, month, year) :
    if (month == 1) :
        month = 13
        year = year - 1
 
    if (month == 2) :
        month = 14
        year = year - 1
    q = day
    m = month
    k = year % 100;
    j = year // 100;
    h = q + 13 * (m + 1) // 5 + k + k // 4 + j // 4 + 5 * j
    h = h % 7
    return h

def getNextDate(y, m, d):
    if m==12:
        return [y+1, 1, 1]
    else:
        return [y, m+1, 1]
    
def solve(ymd1, ymd2):
    y1, m1, d1 = ymd1
    y2, m2, d2 = ymd2
    
    sundays = 0
    
    if d1 == 1:
        if Zellercongruence(d1, m1, y1) == 1:
            sundays += 1
    
    y, m, d = y1, m1, d1
    while True:
        y, m, d = getNextDate(y, m, d)
        
        #check if date over than date2
        if y>y2:
            break
        elif y==y2:
            if m>m2:
                break
            elif m==m2:
                if d>d2:
                    break
                
        if Zellercongruence(d, m, y) == 1:
            sundays += 1
    
    return sundays
     
t = int(input().strip())
for a0 in range(t):
    y1, m1, d1 = [int(num) for num in input().strip().split(' ')]
    y2, m2, d2 = [int(num) for num in input().strip().split(' ')]
    print(solve([y1, m1, d1], [y2, m2, d2]))
    
    