# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 23:36:40 2018

@author: Akshay Jagadale
"""

class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
      
        N = len(grid)

        ans = 0
        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    ans += 2
                    for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r,c+1)):
                        if 0 <= nr < N and 0 <= nc < N:
                            nval = grid[nr][nc]
                        else:
                            nval = 0

                        ans += max(grid[r][c] - nval, 0)
                        
        return ans


                    
        
        
        
myobj = Solution()
print(myobj.surfaceArea([[1,1,1],[1,0,1],[1,1,1]]))