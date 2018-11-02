# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 20:43:28 2018

@author: Akshay Jagadale
"""



def pair_sum(arr,k):
    rset = set()
    tlist = []
    
    if len(arr) < 2:
        return None
    
    for i in range(0,len(arr)):
        if (k-arr[i] not in tlist):
            tlist.append(arr[i])
        elif (k-arr[i] in tlist):
            rset.add((min(k-arr[i],arr[i]),max(k-arr[i],arr[i])))
    
    return rset
    

    
print(pair_sum([1,3,2,2],4))