# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 23:09:23 2018

@author: Akshay Jagadale
"""

class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        
        res = []
        for i in range(0,len(A[0])):
            temp = []
            for j in range(0,len(A)):
                temp.append(A[j][i])
            res.append(temp)
        return(res)
        
myobj =  Solution()
print(myobj.transpose([[1,2,3],[4,5,6]]))