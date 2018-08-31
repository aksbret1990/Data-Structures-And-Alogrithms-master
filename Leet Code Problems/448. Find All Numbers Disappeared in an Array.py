# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 10:40:10 2018

@author: Akshay Jagadale
"""

class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
#        #method 1
#        setall = {i for i in range(1,len(nums)+1)}
#        return(list(setall -  set(nums)))
        
        #method 2
#        for i in nums:
#            index = int(i) - 1
#            nums[index] += 0.0000001
#            
#        res = []
#        for i in range(0,len(nums)):
#            if nums[i] == int(nums[i]):
#                res.append(i+1)
#        return res
        
        #method3: using absolute
        ret = []
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]
        for i in range(len(nums)):
            if nums[i] > 0:
                ret.append(i + 1)
        return ret
        
        
            


        
        
myobj = Solution()
print(myobj.findDisappearedNumbers([4,3,2,7,8,2,3,1]))


