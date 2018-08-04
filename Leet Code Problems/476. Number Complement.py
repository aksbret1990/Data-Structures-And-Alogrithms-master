# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 19:31:17 2018

@author: Akshay Jagadale
"""

class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
#        
        #method1
#        i = 1
#        num1 = num
#        if num == 1:
#            return 0
#        else:
#            while i <= num1:
#                num = num ^ i
#                i = i << 1
#        
#        return num
#    
        #method2
#        def findComplement(self, num):
#        i = 1
#        while i <= num:
#            i = i << 1
#        return (i - 1) ^ num
        
        

    
        #method3
        mask = 1 << len(bin(num)) - 2
        return num ^ (mask-1)
        
myobj = Solution()
print (myobj.findComplement(5))