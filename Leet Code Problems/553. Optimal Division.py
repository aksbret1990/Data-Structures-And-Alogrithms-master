# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 22:23:15 2018

@author: Akshay Jagadale
"""

class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        A = []
        for i in nums:
            A.append(str(i))
        print(A)
        if len(A) <= 2: 
            return '/'.join(A)
        return '{}/({})'.format(A[0], '/'.join(A[1:]))
    
myobj = Solution()
print(myobj.optimalDivision([1000,100,10,2]))