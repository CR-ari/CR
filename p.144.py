# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 18:37:03 2020

@author: 9876a
"""

userInventory = {'arrow': '12','gold coin': '42','rope': '1','torch': '6','dagger': '1'}
def displayInventory():
    print('Inventory:')
    for key in userInventory.keys():
        print(userInventory[key], key)
        number1 = (int(userInventory['arrow']))
        number2 = int(userInventory['gold coin'])
        number3 = int(userInventory['rope'])
        number4 = int(userInventory['torch'])
        number5 = int(userInventory['dagger'])
    total = number1 + number2 + number3 + number4 + number5
    print('Total numebr of items: ' + str(total))

    
displayInventory()

