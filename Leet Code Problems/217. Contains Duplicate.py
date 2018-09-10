# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 17:19:00 2018

@author: Akshay Jagadale
"""

class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mdict = {}
        
        for i in nums:
            if i not in mdict:
                mdict[i] = 1
            else:
                return True
        return False
        
myobj = Solution()
print(myobj.containsDuplicate([1,2,3,1]))