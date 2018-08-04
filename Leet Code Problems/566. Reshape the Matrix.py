# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 12:03:12 2018

@author: Akshay Jagadale
"""

class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        
        
        elements = []
        for i,row in enumerate(nums):
            for j,value in enumerate(row):
                elements.append(value)

        if (i+1) * (j+1) < r * c:
            return nums
        
        else:
            new_elements = []
            for i in range(0,r):
                column = []
                for j in range(0,c):
                    column.append(elements.pop(0))
                new_elements.append(column)
            return new_elements
        
                
                
        
        
myobj = Solution()
print(myobj.matrixReshape([[1,2], [3,4]], 4, 1))