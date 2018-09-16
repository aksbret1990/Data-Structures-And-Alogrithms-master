# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 10:40:05 2018

@author: Akshay Jagadale
"""

class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        
        #method: own......deletion
#        if len(nums1) > len(nums2):
#            large = nums1
#            small = nums2
#        else:
#            large = nums2
#            small = nums1
#            
#        res = []
#        i = 0
#        while i < len(small):
#            #print(small)
#            #print(large)
#            if small[i] in large:
#                #print(small[i])
#                temp = small[i]
#                res.append(temp)
#                small.remove(temp)
#                large.remove(temp)
#                continue
#            i += 1
#            #print()
#        return res
        
        
        
        #method: fastest using dict
        
        dict1 = {}
        for i in nums1:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
                
        res = []
        for i in nums2:
            if i in dict1 and dict1[i] > 0:
                res.append(i)
                dict1[i] -= 1
        return res
        
        
        
myobj = Solution()
print(myobj.intersect([1,2,2,1], [2,2]))