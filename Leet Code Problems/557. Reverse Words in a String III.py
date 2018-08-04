# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 16:36:59 2018

@author: Akshay Jagadale
"""

class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
#        
        #method1
#        mylist =  s.split(" ")
#        res = []
#        for i in mylist:
#            res.append(i[::-1])
#        
#        print(res)
#        final = ' '.join(res)
#        print(final)
            
        
        #method2
        #print ( ' '.join(s.split()[::-1])[::-1] )
        
        
        #method3
        words = s.split()
        return ' '.join( [x[::-1] for x in words] )
            
        
        
myobj = Solution()
print( myobj.reverseWords("Hello how are you") )
