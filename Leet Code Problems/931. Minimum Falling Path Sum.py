# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 17:31:29 2019

@author: Akshay Jagadale
"""

class Solution:
    def minFallingPathSum(self, A):
        for i in range(len(A)-2,-1, -1):
            for j in range(0,len(A[0])):
                if j == 0 :
                    A[i][j] = min(A[i][j]+ A[i+1][j], A[i][j] + A[i+1][j+1])
                    
                elif j == len(A[0]) - 1:
                    A[i][j] = min(A[i][j]+ A[i+1][j], A[i][j] + A[i+1][j-1])
                    
                else:
                    A[i][j] = min(A[i][j]+ A[i+1][j], A[i][j] + A[i+1][j-1],A[i][j] + A[i+1][j+1])
                    
            #print(A)
                    
                    
        return min(A[0])
    
    
myobj = Solution()
print(myobj.minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]))