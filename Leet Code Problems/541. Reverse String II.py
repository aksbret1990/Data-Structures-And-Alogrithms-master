# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 10:37:38 2018

@author: Akshay Jagadale
"""

class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
        import math as m
        
        i = m.ceil(len(s)/(2*k))
        
        newstr = ''
        for i in range(1,i+1):
            orig = s[2*(i-1)*k:2*i*k]
            first_half = orig[0:k]
            second_half = orig[k:]
            first_half_reversed = first_half[::-1]
            #print(first_half_reversed)
            #print(second_half)
            newstr = newstr + first_half_reversed + second_half
        
        return(newstr)
        
        
myobj = Solution()
myobj.reverseStr('abcd',2)