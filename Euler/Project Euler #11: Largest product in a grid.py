#!/bin/python3

import sys

vertical = []
for i in range(340):
    vertical.append([i, i+20, i+40, i+60])
    
horizontal = []
for i in range(400):
    if i%20 > 16:
        continue
    horizontal.append([i, i+1, i+2, i+3])

diagonal_left = []
for i in range(337):
    if i%20 > 16:
        continue
    diagonal_left.append([i, i+21, i+42, i+63])
    
diagonal_right = []
for i in range(340):
    if i%20 < 3:
        continue    
    diagonal_right.append([i, i+19, i+38, i+57])
    
all_combination = vertical + horizontal + diagonal_left + diagonal_right

def solve(grid):
    top=0
    for com in all_combination:
        result = grid[com[0]]*grid[com[1]]*grid[com[2]]*grid[com[3]]
        if result>top:
            top=result
    return top

grid = []
for grid_i in range(20):
	grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
	grid.extend(grid_t)
 
print(solve(grid))