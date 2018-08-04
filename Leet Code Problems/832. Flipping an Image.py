# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 14:20:33 2018

@author: Akshay Jagadale
"""

'''
'''

class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        
        res = []
        
        for a in A:
            a = a[::-1]
            a = [x ^ 1 for x in a]
            res.append(a)
        
        return res
                
        
myobj = Solution()
print(myobj.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))