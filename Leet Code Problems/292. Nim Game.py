# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 13:19:31 2018

@author: Akshay Jagadale
"""

class Solution:
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        return n % 4 != 0
        
myobj = Solution()
res = myobj.canWinNim(10)
print(res)