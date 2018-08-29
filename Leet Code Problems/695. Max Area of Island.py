# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 15:24:17 2018

@author: Akshay Jagadale
"""

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        
        # DFS iterative
        seen = set()
        maxarea = 0
        for r0,row in enumerate(grid):
            for c0,val in enumerate(row):
                if val and (r0,c0) not in seen:
                    shape = 0
                    stack = [(r0,c0)]
                    seen.add((r0,c0))
                    while stack:
                        r,c = stack.pop()
                        shape += 1
                        for nr,nc in [((r-1),c),((r+1),c),(r,(c-1)),(r,(c+1))]:
                            if (0 <= nr < len(grid) and 0 <= nc < len(grid[0])  
                            and grid[nr][nc] and (nr,nc) not in seen):    
                                stack.append((nr,nc))
                                seen.add((nr,nc))
                    maxarea = max(maxarea,shape)
                    
        print(maxarea)
        
        #DFS recursive
#        def maxAreaOfIsland(self, grid):
#        seen = set()
#        def area(r, c):
#            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])
#                    and (r, c) not in seen and grid[r][c]):
#                return 0
#            seen.add((r, c))
#            return (1 + area(r+1, c) + area(r-1, c) +
#                    area(r, c-1) + area(r, c+1))
#
#        return max(area(r, c)
#                   for r in range(len(grid))
#                   for c in range(len(grid[0])))
                                    
                    
                    
        
        
myobj = Solution()
myobj.maxAreaOfIsland([
 [0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]
 ])