# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 13:47:05 2018

@author: Akshay Jagadale
"""

class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        
            

            
        #method1
#        dif = (sum(A) - sum(B)) / 2
#        A = set(A)
#        for b in set(B):
#            if dif + b in A:
#                return [dif + b, b]
        
        #method2
        sumA, sumB  = sum(A), sum(B)
        setA, setB = set(A), set(B)
        total = (sumA + sumB) // 2 # the final same total amount
        
        for i in setA:
            if total - (sumA - i) in setB:
                return [i, total - (sumA - i)]
            
        
        
myobj = Solution()
print(myobj.fairCandySwap([1,2,5],[2,4]))
