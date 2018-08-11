# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 23:28:59 2018

@author: Akshay Jagadale
"""

def reverse(s):
    if len(s) == 0:
        return s
    elif len(s) == 1:
        return s[0]
    else:
        return s[len(s)-1] + reverse(s[:len(s)-1])

print(reverse('hello world'))