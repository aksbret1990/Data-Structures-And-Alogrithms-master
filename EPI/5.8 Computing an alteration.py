# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 14:55:16 2019

@author: Akshay Jagadale
"""

A = [4,5,1,3,2,7,8,6]

def interleaved(A):
    for i in range(len(A)-1):
        if i == 0 and A[i] < A[i+1]:
            continue
        elif i == 0 and A[i] > A[i+1]:
            A[i],A[i+1] = A[i+1],A[i]
        if i == 1 and A[i] > A[i+1]:
            continue
        elif i == 1 and A[i] < A[i+1]:
            A[i],A[i+1] = A[i+1],A[i]        
            
    print(A)
        
interleaved(A)