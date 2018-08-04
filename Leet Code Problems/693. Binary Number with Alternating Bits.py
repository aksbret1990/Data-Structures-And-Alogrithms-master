# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 07:53:48 2018

@author: Akshay Jagadale
"""

class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        binnum = bin(n)
        strbinnum = binnum[:]
        
        
        for i in range(0,len(strbinnum)-1):
            if strbinnum[i] == strbinnum[i+1]:
                return False
            else:
                continue
        return True
    
#        #method2
#        n, cur = divmod(n, 2)
#        while n:
#            if cur == n % 2: return False
#            n, cur = divmod(n, 2)
#        return True
        
myobj = Solution()
res = myobj.hasAlternatingBits(0)
print(res)