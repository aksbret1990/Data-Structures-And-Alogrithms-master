# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 14:40:22 2018

@author: Akshay Jagadale
"""

class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        
        
  
        
    

        x = x ^ y
        y = 0
        while x:
            print('x before:' ,x)
            print('y before:' ,y)
            y += 1
            x = x & (x - 1)
            print('x after:' ,x)
            print('y after:' ,y)
            
        print('x :' ,x)
        print('y :' ,y)
        
        """
        
        
        print('x: ',bin(x))
        print('y: ',bin(y))
        print('x ^ y :',bin(x^y))
        print('x ^ y :',bin(x^y).count('1'))
        return bin(x^y).count('1')
        
my = Solution()
my.hammingDistance(1,4)
