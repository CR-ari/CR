# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 16:56:38 2020

@author: 9876a
"""

print('List Name: ')
name = input()

print('List Element: ')
element1 = input()

name = []
name.append(element1)

print('Do you want to add more elements? [Y/N]')
choice = input()

while choice == 'Y':
    print('Element: (If you want to stop, type N)')
    element2 = input()
    name.append(element2)
    
    if element2 == 'N':
        name.pop()
        break
    else:
        print('type more elements')

        
if len(name) >= 2:
    name.insert(-1, 'and')
    name1 = ' '.join(name)
    name2 = name1.replace(' ',',')
    print(name2)
else:
    name1 = ' '.join(name)
    name2 = name1.replace(' ', ',')
    print(name2)
