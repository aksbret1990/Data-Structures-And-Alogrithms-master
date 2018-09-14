# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 16:44:45 2018

@author: Akshay Jagadale
"""

class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        count = 0
        for i in range(len(points)):
            h = {}
            for j in range(len(points)):
                if i != j:
                    dt = pow(points[i][0] - points[j][0], 2) + pow(points[i][1] - points[j][1], 2)
                    count += h.get(dt, 0)
                    h[dt] = h.get(dt, 0) + 1
            print(h)
            print(count)
            print()
        return count*2
    
myobj = Solution()
print(myobj.numberOfBoomerangs([[0,0],[1,0],[2,0]]))
