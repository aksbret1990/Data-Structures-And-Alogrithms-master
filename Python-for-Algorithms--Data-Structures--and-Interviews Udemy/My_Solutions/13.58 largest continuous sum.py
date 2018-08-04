# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 20:10:17 2018

@author: Akshay Jagadale
"""

def large_cont_sum(arr):
#    res = []
#    for i in range(len(arr)):
#        lcs = arr[i]
#        for j in range(i+1,len(arr)):
#            if sum(arr[i:j]) > lcs:
#                lcs = sum(arr[i:j])
#        res.append(lcs)
#    return max(res)
          
    if len(arr) == 0:
        return 0
    
    max_sum = current_sum = arr[0]
    start_index = 0
    end_index = 0
    for i in range(1,len(arr)):
        if current_sum+arr[i] < arr[i]:
            start_index = i
        current_sum = max(current_sum+arr[i],arr[i])
        if current_sum > max_sum:
            end_index = i
        max_sum = max(current_sum, max_sum)

    return max_sum   
    #return arr[start_index:end_index+1]

print(large_cont_sum([1,2,-1,3,4,10,10,-10,-1]))