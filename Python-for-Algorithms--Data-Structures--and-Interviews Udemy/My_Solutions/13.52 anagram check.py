# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 10:37:18 2018

@author: Akshay Jagadale
"""

def anagram(s1,s2):
#    l1 = [x for x in s1]
#    l2 = [x for x in s2]
#    
#    l1.sort()
#    l2.sort()
#    if l1 == l2:
#        return True
#    return False
    

    if(len(s1) != len(s2)):
        return False
    
    dict1 = {}

    
    s1 = s1.replace(" ","").lower()
    s2 = s2.replace(" ","").lower()
    for i in s1:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
            
    for i in s2:
        if i in dict1:
            dict1[i] -= 1
        else:
            dict1[i] = 1
            
    for i in dict1:
        if dict1[i] > 0:
            return False
    return True
    
    
    
    
print(anagram('clint east wood','old west action'))
