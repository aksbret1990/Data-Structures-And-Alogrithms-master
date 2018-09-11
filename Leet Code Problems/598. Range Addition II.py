# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 16:31:04 2018

@author: Akshay Jagadale
"""

class Solution:
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        
#        #Approach #1 Brute Force [Time Limit Exceeded]
#        mat = []
#        for i in range(0,m):
#            row = []
#            for j in range(0, n):
#                row.append(0)
#            mat.append(row)
#        #print(mat)
#        
#        for i,row in enumerate(ops):
#            rowsize = row[0]
#            colsize = row[1]
#            for i in range(0, rowsize):
#                for j in range(0,colsize):
#                    mat[i][j] += 1           
#        print(mat)
#                
#        from collections import OrderedDict
#        cdict = {}
#        for i, row in enumerate(mat):
#            for j,k in enumerate(row):
#                if k not in cdict:
#                     cdict[k] = 1
#                else:
#                    cdict[k] += 1
#                     
#        #print(cdict)
#        sdict = OrderedDict(sorted(cdict.items(), key = lambda t : t[0], reverse = True))
#        #print(sdict)
#        #print(next(iter(sdict.values())))
#        return next(iter(sdict.values()))
            
        #Approach #2 Single Pass [Accepted]
#        if not ops:
#            return m*n
#        return min(op[0] for op in ops)*min(op[1] for op in ops)
        
  
myobj = Solution()
print(myobj.maxCount(3,3,[[2,2],[3,3]]))