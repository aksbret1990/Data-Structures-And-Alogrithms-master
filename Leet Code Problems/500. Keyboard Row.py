# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 17:19:17 2018

@author: Akshay Jagadale
"""


class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
#        
#        method1
#        return [
#                w for w in words 
#                
#                if 
#                    all(x.lower() in list('qwertyuiop') for x in w)
#                or 
#                    all(x.lower() in list('asdfghjkl') for x in w)
#                or
#                    all(x.lower() in list('zxcvbnm') for x in w)
#                    
#                ]
        
        #method2
#        return[
#            w for w in words if any( set(w.lower()).issubset(row) for row in [set('qwertyuiop'),set('asdfghjkl'),set('zxcvbnm')] )
#                ]
        
        
        
 
myobj = Solution()
print ( myobj.findWords(["Hello", "Alaska", "Dad", "Peace"])  )