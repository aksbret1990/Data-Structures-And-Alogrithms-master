# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 05:29:14 2018

@author: Akshay Jagadale
"""

#def fib(n):
#    if n==1 or  n==0:
#        return n
#    else:
#        return fib(n-1) + fib(n-2)
    
cache = {}

def fib(n):
    
    if n==0 or n==1:
        return n
    
    if n not in cache.items():
        cache[n] = fib(n-1) + fib(n-2)
        return cache[n]

    else:
        return cache[n]

    
print(fib(7))