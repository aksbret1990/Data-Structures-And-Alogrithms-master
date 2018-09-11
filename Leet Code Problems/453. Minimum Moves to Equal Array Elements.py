# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 13:53:22 2018

@author: Akshay Jagadale
"""

class Solution:
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #Is to find the law, summing each element minus the smallest element is the number of times the smallest element needs to move, lol ~ :-)
        minum = min(nums)
        ret = 0 
        for i in nums:
            ret += i - minum
        return ret
                
        #return sum(nums)-len(nums)*min(nums)
        
        
myobj = Solution()
print(myobj.minMoves([1,2,3]))