# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 17:11:31 2018

@author: Akshay Jagadale
"""

class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s[::-1]
        sum = 0
        for exp, char in enumerate(s):
            sum += (ord(char) - 65 + 1) * (26 ** exp)
            return sum
        
        
myobj = Solution()
print(myobj.titleToNumber('Z'))
