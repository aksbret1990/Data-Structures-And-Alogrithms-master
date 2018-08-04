# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 12:50:50 2018

@author: Akshay Jagadale
"""

class Solution:
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        
        if a == b:
            return -1
        
        if len(a) != len(b):
            return max(len(a),len(b))
        
        if len(a) == len(b):
            return len(a)
        
            
        
        
        
myobj = Solution()
res = myobj.findLUSlength("aefawfawfawfaw","aefawfeawfwafwaef")
print(res)




