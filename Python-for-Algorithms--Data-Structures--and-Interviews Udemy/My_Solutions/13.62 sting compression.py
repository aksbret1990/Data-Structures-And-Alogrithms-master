# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 20:51:12 2018

@author: Akshay Jagadale
"""

def compress(A):
#    i = 0
#    rstr = ''
#    while i < len(A) - 1:
#        num = 1
#        while A[i].lower() == A[i+1].lower():
#            num += 1
#            i += 1
#            if i+1 == len(A):
#                break
#        rstr = rstr + A[i].upper() + str(num)
#        print(rstr)
#        i += 1
#    return rstr

    
    if len(A) == 0:
        return ''
    
    if len(A) == 1:
        return A[0] + '1'
    res = ''
    num = 1
    for i in range(0,len(A)):
        if i + 1 == len(A):
            res += A[i] + str(num)
        elif A[i] ==  A[i+1]:
            num += 1
        else:
            res += A[i] + str(num)
            num = 1
    return res
    
print(compress('AABCCCC'))