# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 16:09:17 2019

@author: Akshay Jagadale
"""

A = [40,20,30,10]
perm = [1,3,0,2]


def apply_permuatation(A, perm):
    for i in range(len(A)):
        iterator = i
        while iterator != perm[iterator]:
            index = perm[iterator]
            tempval = A[index]
            tempindex = perm[index]
            A[index] = A[iterator]
            perm[index] = index
            A[iterator] = tempval
            perm[iterator] = tempindex
    
    print(A)        
    
apply_permuatation(A,perm)
    
