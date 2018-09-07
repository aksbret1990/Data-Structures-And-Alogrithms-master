# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 14:06:59 2018

@author: Akshay Jagadale
"""

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        profit = 0        
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit
            
        
myobj = Solution()
print(myobj.maxProfit([7,1,5,4,3,2,3,6,4]))