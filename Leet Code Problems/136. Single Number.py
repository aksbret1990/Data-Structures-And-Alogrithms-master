# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 08:22:11 2018

@author: Akshay Jagadale
"""

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mydict = {}
        for i in nums:
            if i not in mydict:
                mydict[i] = 1
            else:
                mydict[i] += 1
                
      
                
        x = min(mydict, key=mydict.get)
        return x
        
myobj = Solution()
res = myobj.singleNumber([1,2,3,4,4,2,2,1,1,1])
print(res)