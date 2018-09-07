# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 13:52:34 2018

@author: Akshay Jagadale
"""

class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        #method using set inbuilt function
        #return list(set(nums1).intersection(nums2))
    
        #method
#        resset = set()
#        for i in nums1:
#            if i in nums2:
#                resset.add(i)
#        return list(resset)
        
        
        
myobj = Solution()
print(myobj.intersection([4,9,5], [9,4,9,8,4]))