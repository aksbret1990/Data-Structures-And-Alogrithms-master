# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 12:26:36 2018

@author: Akshay Jagadale
"""

class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
#        res = []
#        for i in range(1, n+1):
#            
#            if i % 3 == 0 and i %5 == 0:
#                res.append('FizzBuzz')
#            
#            elif i % 3 == 0:
#                res.append('Fizz')
#                
#            elif i % 5 == 0:
#                res.append('Buzz')
#                
#            else:
#                 res.append(str(i))  
#                
#        return res 
    
        
        
        return [('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0)) or str(i) for i in range(1, n+1)]
        
        
        
myobj = Solution()
print (myobj.fizzBuzz(15))