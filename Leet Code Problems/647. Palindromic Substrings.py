# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 08:22:39 2018

@author: Akshay Jagadale
"""

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        N = len(s)
        ans = 0
        for center in range(2*N - 1):
            left = int(center / 2)
            right = int(left + center % 2)
            while left >= 0 and right < N and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1
        return ans   
        
        
      
    
myobj = Solution()
print(myobj.countSubstrings('aaa'))