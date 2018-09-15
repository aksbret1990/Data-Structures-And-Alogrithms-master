# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 13:41:06 2018

@author: Akshay Jagadale
"""

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        import collections
        freq = collections.Counter(s)
        print(freq)
        has_odd_letter_count = False
        length = 0
        for letter, count in freq.items():
            if count % 2 == 1:
                has_odd_letter_count = True
                count -= 1
            length += count
        return length + 1 if has_odd_letter_count else length
        
        #Approach #1: Greedy [Accepted]
#        from collections import Counter
        
#        x = Counter(s)
        #print(x)
        
#        ans = 0
#        for k,v in x.items():
#            ans += v//2 * 2
#            if ans % 2 == 0 and v % 2 == 1:
#                ans += 1
#        return ans
#        
        

                
        
myobj = Solution()
print(myobj.longestPalindrome("abccccdd"))