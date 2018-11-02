# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 21:59:11 2018

@author: Akshay Jagadale
"""

def uni_char(s):
    
    # method1
    #return set(s) == len(s)
    
    vlist = []
    for i in range(0,len(s)):
        if s[i] not in vlist:
            vlist.append(s[i])
        else:
            return False
    return True


print(uni_char('abcdeghijklopp'))
    
    