# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 15:30:44 2018

@author: Akshay Jagadale
"""

from pythonds.basic.stack import Stack

def divideBy2(decNumber):
    
    remstack = Stack()
    
    
    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2
    
    binString = ''
    while not remstack.isEmpty():
        binString += str(remstack.pop())

    return binString
    
print(divideBy2(9))