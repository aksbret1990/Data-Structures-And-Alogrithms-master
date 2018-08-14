# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 23:42:19 2018

@author: Akshay Jagadale
"""

n = 0
gdict = {}
def rec_coin(target, coins):
    global n
    coins.sort()
 
    if target in coins :
        return 1
    if target == 0:
        return 0
    if (len(coins)) == 0:
        return n

    while target < coins[len(coins)-1]:
        coins = coins[:len(coins)-1]
    
    largest = coins[len(coins)-1]
    n = n + int(target/largest) + rec_coin(target % largest,coins[:len(coins) - 1])
    return n

print(rec_coin(74,[1,5,10,25]))




