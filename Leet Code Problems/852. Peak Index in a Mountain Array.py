# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 14:20:33 2018

@author: Akshay Jagadale
"""

'''
'''

class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        #method1
        #return A.index(sorted(A)[-1])
        
        #method 2 linear scan
#        for i in range(0,len(A)):
#            if A[i] > A[i+1]:
#                return i
             
        #method 3 binary search
        lo, hi = 0, len(A) - 1
        while lo < hi:
            mi = int((lo + hi) / 2)
            if A[mi] < A[mi + 1]:
                lo = mi + 1
            else:
                hi = mi
        return lo
        
myobj = Solution()
print(myobj.peakIndexInMountainArray([0,1,0]))