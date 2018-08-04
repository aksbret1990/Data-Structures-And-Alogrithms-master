# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 14:07:47 2018

@author: Akshay Jagadale
"""

class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        
        diag = {}
        for r,row in enumerate(matrix):
            print('r: ' ,r)
            for c,val in enumerate(row):
                print('c: ' ,c)
                if r - c not in diag:
                    diag[r-c] = val
                elif diag[r-c] != val:
                    return False
        return True
    
    def printMatrixself(self, matrix):
        for r,row in enumerate(matrix):
            print()
            for c,val in enumerate(row):
                print(val, end = ' ')
        print()        
    
obj = Solution()
obj.printMatrixself([[1,2,3,4],[5,1,2,3],[9,5,1,2]])
print(obj.isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))