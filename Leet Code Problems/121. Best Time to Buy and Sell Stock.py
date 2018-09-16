# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 11:09:07 2018

@author: Akshay Jagadale
"""

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == [] or len(prices) == 1:
            return 0
        
        minpricesofar = float('inf')
        maxprofit = 0
        
        for price in prices:
            profit_today = price - minpricesofar
            maxprofit = max(maxprofit, profit_today)
            minpricesofar = min(minpricesofar, price)
                
        return maxprofit
        
        
myobj = Solution()
print(myobj.maxProfit([3,2,6,5,0,3]))