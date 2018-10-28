# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 16:10:16 2018

@author: Akshay Jagadale
"""

from pythonds.basic.stack import Stack

def baseConverter(decNumber,base):
    digits = "0123456789ABCDEF"

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]

    return newString

print(baseConverter(25,2))
print(baseConverter(25,8))
print(baseConverter(256,16))
print(baseConverter(26,26))