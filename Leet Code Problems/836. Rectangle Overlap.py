# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 15:18:59 2018

@author: Akshay Jagadale
"""

class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        
        #Approach #1: Check Position [Accepted]
#        return not (rec1[2] <= rec2[0] or  # left
#                    rec1[3] <= rec2[1] or  # bottom
#                    rec1[0] >= rec2[2] or  # right
#                    rec1[1] >= rec2[3])    # top   
        
        #Approach #2: Check Area [Accepted]
        def intersect(p_left, p_right, q_left, q_right):
            return min(p_right, q_right) > max(p_left, q_left)
        return (intersect(rec1[0], rec1[2], rec2[0], rec2[2]) and # width > 0
                intersect(rec1[1], rec1[3], rec2[1], rec2[3]))    # height > 0

        
myobj = Solution()
print(myobj.isRectangleOverlap([7,8,13,15],[10,8,12,20]))