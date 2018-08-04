# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 18:03:45 2018

@author: Akshay Jagadale
"""

class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[::2])
    
myobj = Solution()
print (myobj.arrayPairSum([1,4,3,2]))

        