# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 20:43:28 2018

@author: Akshay Jagadale
"""



def finder(arr1,arr2):
    
#    arr1.sort()
#    arr2.sort()
#    
#    for i in range(len(arr1)):
#        if(arr1[i] - arr2[i]) != 0:
#            return arr1[i]
#        if IndexError:
#            return arr1[len(arr1)-1]
#    return None


#    arr1.sort()
#    arr2.sort()  
#
#    for num1,num2 in zip(arr1,arr2):
#        if num1 != num2:
#            return num1
#    
#    return arr1[-1]
#    
    
    
    
#    dict1 = {}
#    
#    for i in arr1:
#        if i in dict1:
#            dict1[i] += 1 
#        else:
#            dict1[i] = 1
#            
#    for i in arr2:
#       dict1[i] -= 1
#    
#    for k,v in dict1.items():
#        if v > 0:
#            return k
    
    
#    import collections
#    
#    d = collections.defaultdict(int)
#    # if a key is not present in d it will add it a value 0
#    
#    
#    for num in arr2:
#        d[num] += 1
#        
#    for num in arr1:
#        if d[num] == 0:
#            return num
        
    result = 0
    
    for num in arr1 + arr2:
        result = result ^ num
        #print(result)
    return result
        
    
    #approach 3: diff(sum(arr1),sum(arr2). overflow issues so avoid
    
print(finder([5,5,7,4,7,6,8],[5,5,7,4,7,6]))