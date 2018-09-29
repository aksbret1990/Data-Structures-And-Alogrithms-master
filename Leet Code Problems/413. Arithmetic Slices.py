# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 11:14:42 2018

@author: Akshay Jagadale
"""

class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        
#        #brute force
#        
#        count  = 0
#        
#        for s in range(0,len(A)-2):
#            d = A[s+1] - A[s]
#            for e in range(s+2,len(A)):
#                if d == A[e] - A[e-1]:
#                    count += 1
#                else:
#                    break
#        return count
        
        #Approach #5 Dynamic Programming [Accepted]:
#        dp = [0]  * len(A)
#        suma = 0
#        for i in range(2,len(A)):
#            if A[i] - A[i-1] == A[i-1] - A[i-2]:
#                dp[i] = dp[i-1] + 1
#                suma += dp[i]
#        return suma
        
        
        
        #Approach #5 Constant Space Dynamic Programming [Accepted]:
        dp = 0 
        suma = 0
        for i in range(2,len(A)):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                dp = dp + 1
                suma = suma + dp
            else:
                dp = 0
        return suma
        
        
        
        
        
        
        
        
myobj = Solution()
print(myobj.numberOfArithmeticSlices([1, 2, 3, 4]))