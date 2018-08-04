# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 21:24:02 2018

@author: Akshay Jagadale
"""

class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        
        p = []
        def find(h, t):
            if not t or t.isdigit(): p.append(h + t)
            for i in range(len(t)):
                if t[i].isalpha():
                    find(h + t[:i+1],t[i+1:])
                    find(h + t[:i+1].swapcase(), t[i+1:])     
                    break
        find("", S)
        return p
        
myobj = Solution()
print(myobj.letterCasePermutation('a1b2'))