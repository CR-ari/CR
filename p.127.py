# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 16:14:48 2020

@author: 9876a
"""

grid = [['.','.','.','.','.','.'],
        ['.','0','0','.','.','.'],
        ['0','0','0','0','.','.'],
        ['0','0','0','0','0','.'],
        ['.','0','0','0','0','0'],
        ['0','0','0','0','0','.'],
        ['0','0','0','0','.','.'],
        ['.','0','0','.','.','.'],
        ['.','.','.','.','.','.']]


grid3 = []

for i in range(0,6,1):
    for j in range(8,-1,-1):
        grid2 = grid[j][i]
        grid3.append(grid2)
        if i == 6 and j == -1:
            break


print(''.join(grid3[0:9]))
print(''.join(grid3[9:18]))
print(''.join(grid3[18:27]))
print(''.join(grid3[27:36]))
print(''.join(grid3[36:45]))
print(''.join(grid3[45:54]))



