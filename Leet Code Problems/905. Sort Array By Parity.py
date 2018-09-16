# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 10:04:50 2018

@author: Akshay Jagadale
"""

class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        i = 0
        j = len(A)-1
   
        while i < j:
            while A[i] % 2 == 0 and i < len(A) -1:
                i += 1
            while A[j] % 2 == 1 and j > 0:
                j -= 1 
            if i >= j:
                break
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1
        return A
        
        
        
myobj = Solution()
print(myobj.sortArrayByParity([0,1]))

[8,1,2,5,6,4,3,9]