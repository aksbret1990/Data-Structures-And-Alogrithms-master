# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 16:26:11 2018

@author: Akshay Jagadale
"""

class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        acount = 0
        lcount = 0
        for i in range(0,len(s)):
            if s[i] == 'A':
                acount += 1
            if s[i] == 'L' and i <= len(s) - 3:
                if s[i+1] == s[i+2] == 'L':
                    lcount = 1
        if acount <= 1 and not lcount:
            return True
        return False
        
myobj = Solution()
print(myobj.checkRecord('PPALLL'))