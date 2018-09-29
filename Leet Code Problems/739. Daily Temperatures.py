# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 10:05:52 2018

@author: Akshay Jagadale
"""

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        
        #stack
        ans = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                cur = stack.pop()
                ans[cur] = i - cur
            stack.append(i)
                    
            

        
        
myobj = Solution()
print(myobj.dailyTemperatures([89,62,70,58,47,47,46,76,100,70]))