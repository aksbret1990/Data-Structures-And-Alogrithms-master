# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 20:54:30 2018

@author: Akshay Jagadale
"""

class Solution:
    def toLowerCase(self, str):
       
        '''
        #method1
        return str.lower()
        '''  
        
        #method2
        
        res = ''
        for s in str:
            if ord(s) <= ord('Z') and ord(s) >= ord('A'):
                res += chr(ord(s) - ord('A') + ord('a'))
            else:
                res += s
        return res
    
myobj = Solution()        
print(myobj.toLowerCase('AKSHAY'))