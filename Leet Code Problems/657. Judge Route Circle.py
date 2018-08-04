# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 12:29:38 2018

@author: Akshay Jagadale
"""

class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        
        mydict = {'U':0,'D':0,'R':0,'L':0}
        for i in range(len(moves)):
            mydict[moves[i]] += 1
        
        print(mydict)
        if mydict['U'] == mydict['D'] and mydict['L'] == mydict['R'] :
            print('True')
            return True
        else:
            print('False')
            return False
        
myobj = Solution()
myobj.judgeCircle('UDRLUDL')
        
