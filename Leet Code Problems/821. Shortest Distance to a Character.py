# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 23:36:56 2018

@author: Akshay Jagadale
"""

class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        
        res = []
        dist = []
        
        for i in range(0,len(S)):
            if S[i] == C:
               dist.append(i)
               
        print(dist)
        for i in range(0,len(S)):
            res.append(min([abs(i - y) for y in dist]))
        
        return res

myobj = Solution()
print(myobj.shortestToChar('loveleetcode','e'))

