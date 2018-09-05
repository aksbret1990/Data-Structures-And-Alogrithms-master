# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 15:06:06 2018

@author: Akshay Jagadale
"""

class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        trend = set()
        for i in range(1,len(A)):
            if A[i-1] < A[i]:
                trend.add('increasing')
            elif A[i-1] == A[i]:
                trend.add('equal')
            else:
                trend.add('decreasing')
                
        print(trend)
        
        if 'increasing' in trend and 'decreasing' in trend:
            return False
        return True
                
            
            
        
myobj = Solution()
print(myobj.isMonotonic([6,5,4,4]))