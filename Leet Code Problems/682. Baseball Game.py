# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 14:29:24 2018

@author: Akshay Jagadale
"""

class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        
        res = []

        
        for i in range(len(ops)):
            
            if ops[i] == '+':
                res.append(int(res[len(res)-2]) + int(res[len(res)-1]))
                
            elif ops[i] == 'D':
                res.append(int(res[len(res)-1]) * 2) 
                
            elif ops[i] == 'C':
                res.remove(res[len(res)-1])
                
            else:
                res.append(int(ops[i]))
                
            print(res)
                 
        return sum(res)
            
        

            
myobj =  Solution()
print(myobj.calPoints(["5","-2","4","C","D","9","+","+"]))