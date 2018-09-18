# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 11:54:33 2018

@author: Akshay Jagadale
"""

class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
 
        #dynamic programming
        f1 = cost[0]
        f2 = cost[1]
        for i in range(2,len(cost)):
            f_current = cost[i] + min(f1,f2)
            f1 = f2
            f2 = f_current
        return min(f1, f2);
        
myobj = Solution()
print(myobj.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))




