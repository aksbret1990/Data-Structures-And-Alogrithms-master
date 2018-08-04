# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 18:46:27 2018

@author: Akshay Jagadale
"""

class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
#        method 1: pythonic
#        return s[::-1]
        
        
        #method2: classic
#        res = list(s)
#        i = 0 
#        j = len(s) - 1
#        
#        while i < j:
#            res[i],res[j] = res[j],res[i]
#            i+=1
#            j-=1
#            
#        return "".join(res)
    
        
        #method3: classic short
#        return "".join(list(reversed(list(s))))
        
#        method4: recursive
#        l = len(s)
#        if l < 2:
#            return s
#        return self.reverseString(s[int(l/2):]) + self.reverseString(s[:int(l/2)])
        
        
        
myobj = Solution()
print(myobj.reverseString('hello'))