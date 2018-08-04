# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 12:49:39 2018

@author: Akshay Jagadale
"""

class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        
        
        
        print('A initially:',A)
        print('B initially:',B)
        
        for i in range(len(A)):
            if A==B:
                print ('True')
                return True
            else:
                A = A[1:len(A)] + A[0]
                print('pass: ' , i)
                print('A :',A)
                print('B :',B)
                print('---------------')

        print ('False')
        return False
        
        """
        
        return len(A) == len(B) and B in A + A
        
myobj = Solution()
myobj.rotateString('abcde','abced')
        
