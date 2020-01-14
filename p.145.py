# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 15:03:56 2020

@author: 9876a
"""
inven = {'gold coin': '42','rope': '1'}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
dragonlist = {} 

coin = 0
dagger = 0
ruby = 0
def addToInventory():
    coin = dragonLoot.count('gold coin')
    dagger = dragonLoot.count('dagger')
    ruby = dragonLoot.count('ruby')
    dragonlist['gold coin'] = int(coin)
    dragonlist['dagger'] = int(dagger)
    dragonlist['ruby'] = int(ruby)
    
    inven['gold coin']= int(inven['gold coin']) + int (coin)
    
    dragonlist.update(inven)
    print(dragonlist)
        

def displayInventory():        
    print('Inventory:')
    item_total = 0
    for k, v in dragonlist.items():
        print(str(v) + ' ' + k)
        item_total += int(v)
        
    print("Total number of items: " + str(item_total))


addToInventory()
displayInventory()