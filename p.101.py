# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 15:52:19 2020

@author: 9876a
"""

def collatz():
    print('Enter number:')
    number = int(input())
    if (number % 2) == 0 :
        print(number // 2)
    else :
        print(number *3 +1)
        
collatz()