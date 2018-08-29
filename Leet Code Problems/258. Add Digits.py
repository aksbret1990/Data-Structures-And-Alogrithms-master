# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 16:59:56 2018

@author: Akshay Jagadale
"""

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        #method 1
#        while len(str(num)) > 1:
#            add = 0
#            x = str(num)
#            for i in x:
#                add += int(i)
#            num = add
#            
#       # print(num)
#        return num   
        
        
        #method 2:
        
        if num == 0:
            return 0
        elif num % 9 == 0:
            return 9
        else:
            return num % 9
        
        #method 3
        # return self.addDigits(sum(int(i) for i in str(num))) if num>=10 else num 
        
myobj = Solution()
print(myobj.addDigits(49))