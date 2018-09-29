# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 12:32:58 2018

@author: Akshay Jagadale
"""

class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        
        target_dist = abs(target[0]) + abs(target[1])
        
        for r, c in ghosts:
            ghost_target = abs(target[0] - r) + abs(target[1] - c)
            if ghost_target <= target_dist:
                return False
            
        return True
        
myobj = Solution()
print(myobj.escapeGhosts( [[1, 0], [0, 3]], [0, 1]))