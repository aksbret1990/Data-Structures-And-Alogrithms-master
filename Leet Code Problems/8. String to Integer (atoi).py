# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 23:53:29 2018

@author: Akshay Jagadale
"""

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        
        ls = list(str.strip())
        if len(ls) == 0:
            return 0 
        
        if ls[0] == '-':
            sign = -1
        else:
            sign = 1
            
        if ls[0] in ['+','-']:
            del ls[0]
            
        ret, i = 0,0 
        
        while i < len(ls) and ls[i].isdigit():
            ret = ret * 10 + ord(ls[i]) - ord('0')
            i += 1
            
        return max(-2**31,min(ret * sign, 2**31-1))
        

            
        
myobj = Solution()
print(myobj.myAtoi('1112to'))