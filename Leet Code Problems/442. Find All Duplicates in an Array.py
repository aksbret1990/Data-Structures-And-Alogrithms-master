# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 16:25:20 2018

@author: Akshay Jagadale
"""

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        mdict = {}
        result = []
        for i in nums:
            if i not in mdict:
                mdict[i] = 1
            else:
                mdict[i] += 1
                result.append(i)
                
        return list(set(result))




myobj = Solution()
print(myobj.findDuplicates([4,3,2,7,8,2,3,1]))