# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 16:42:19 2019

@author: Akshay Jagadale
"""

class A:
    def maxSubArray(self, nums):
        calc = nums[0]
        maxn = nums[0]
        for i in range(1,len(nums)):
            calc =  max(nums[i], nums[i] + calc)
            maxn = max(maxn, calc)
            
        return(maxn)

myobj = A()
print(myobj.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
        