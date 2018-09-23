# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 17:50:30 2018

@author: Akshay Jagadale
"""

N = 22

def solution(N):
    # write your code in Python 3.6
    
    '''
    print(str(bin(N))[2:])
    st = str(bin(N))[2:]
    i = 0 
    while st[i] != '1':
        i+=1
        
    gap = 0    
    if i == len(st) - 2:
        return gap
        

    j = i + 1
    curgap = 0
    while j != len(st) - 1:
        
        if st[j] == '0':
            curgap += 1
        else:
            gap = max(gap, curgap)
            curgap = 0
        j +=1 
        
    return gap
    '''
    
    #Approach 1: Store Indexes
#    A= []
#    for i in range(32):
#        if (N >> i) & 1 == 1:
#            A.append(i)
#    print(A)
#    
#    if len(A) == 0:
#        return 0
#    gap = 0
#    for i in range(0,len(A)-1):
#        gap = max(gap,A[i+1] - A[i] -1)
#        
#    return gap

    #Approach 2: One Pass
    last = None
    ans = 0
    for i in range(32):
        if (N >> i) & 1:
            if last is not None:
                ans = max(ans, i - last)
            last = i
    return ans
    
    
    
    
        

print(solution(N))