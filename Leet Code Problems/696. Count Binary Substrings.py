# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 14:45:53 2018

@author: Akshay Jagadale
"""

# Approach #1: Group By Character [Accepted]

class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        #method1: Approach #1: Group By Character [Accepted]
#        groups = [1]
#        for i in range(1, len(s)):
#            if s[i-1] != s[i]:
#                groups.append(1)
#            else:
#                groups[-1] += 1
#
#        ans = 0
#        for i in range(1, len(groups)):
#            ans += min(groups[i-1], groups[i])
#        return ans
    
    
#        #method2: Linear Scan [Accepted]
#        ans, prev, cur = 0, 0, 1
#        for i in range(1, len(s)):
#            if s[i-1] != s[i]:
#                ans += min(prev, cur)
#                prev, cur = cur, 1
#            else:
#                cur += 1
#
#        return ans + min(prev, cur)
        
        s = list(map(len, s.replace('01', '0 1').replace('10', '1 0').split()))
        #return sum(min(a, b) for a, b in zip(s, s[1:]))
        print(list(zip(s, s[1:])))
        
myobj = Solution()
myobj.countBinarySubstrings('110001111000000')