# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 08:49:21 2018

@author: Akshay Jagadale
"""

class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        
        different = len(set(candies))
        
        if different > int(len(candies) / 2):
            return int(len(candies) / 2)
        
        else:
           return different         
            
        
                                
        
        
obj = Solution()
print(obj.distributeCandies([1,1,1,1,1,1,1,1,2]))
