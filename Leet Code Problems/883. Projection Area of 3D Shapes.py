# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 14:11:56 2018

@author: Akshay Jagadale
"""

class Solution:
    def projectionArea(self, grid):
        
        
        
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        #method 1
        # return sum(map(max, grid)) + sum(map(max, zip(*grid))) + sum(v > 0 for row in gird for v in grid)
        
        adict = {'top_area' : 0, 'side_area' : 0, 'other_side_area':0}
        
        row_max = -9999999999
        col_max = -9999999999
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] > row_max:
                    row_max = grid[i][j]
                if grid[i][j] > 0:
                    adict['top_area'] += 1
            adict['side_area'] += row_max
            row_max = -9999999999
            
        one_cell = grid[0]    
        for j in range(len(one_cell)):
            for i in range(len(grid)):
                if grid[i][j] > col_max:
                    col_max = grid[i][j]
            adict['other_side_area'] += col_max
            col_max = -9999999999
            
                    
        
        return adict['side_area'] + adict['top_area'] + adict['other_side_area']
 
        
        
myobj = Solution()
print(myobj.projectionArea([[1,4],[1,1]]))


