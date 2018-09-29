# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 13:17:03 2018

@author: Akshay Jagadale
"""

class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        
        stack = [0] #The score of the current frame

        for x in S:
            if x == '(':
                stack.append(0)
            else:
                v = stack.pop()
                stack[-1] += max(2 * v, 1)

        return stack.pop()
    
myobj  = Solution()
print(myobj.scoreOfParentheses('(()(()))'))