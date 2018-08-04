# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 12:03:35 2018

@author: Akshay Jagadale
"""

class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """

#        A = [i for i in range(0,32) if (N >> i) & 1]
#        
#        if len(A) < 2:
#            return 0 
#        return max([abs(A[i+1] - A[i]) for i in range(len(A)-1)])
    
        print(bin(N))
        index = [i for i, v in enumerate(bin(N)) if v == '1']
        return index
myobj = Solution()
print(myobj.binaryGap(6))