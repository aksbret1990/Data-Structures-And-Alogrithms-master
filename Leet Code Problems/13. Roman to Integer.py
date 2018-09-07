# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 10:44:54 2018

@author: Akshay Jagadale
"""

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        numdict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        i = len(s)-1
        num =  0
        while i >= 0:
            letter = s[i]
            if s[i-1] == 'I' and s[i] == 'V' and i!= 0  :
                num += 4
                i -= 2
            elif s[i-1] == 'I' and s[i] == 'X' and i!= 0  :
                num += 9
                i -= 2
            elif s[i-1] == 'X' and s[i] == 'L' and i!= 0  :
                num += 40
                i -= 2
            elif s[i-1] == 'X' and s[i] == 'C' and i!= 0  :
                num += 90
                i -= 2
            elif s[i-1] == 'C' and s[i] == 'D' and i!= 0  :
                num += 400
                i -= 2
            elif s[i-1] == 'C' and s[i] == 'M' and i!= 0  :
                num += 900
                i -= 2
            else:
                num += numdict[letter]
                i = i-1
                
        return num
    
        #method 2:
        
#        roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
#        z = 0
#        for i in range(0, len(s) - 1):
#            if roman[s[i]] < roman[s[i+1]]:
#                z -= roman[s[i]]
#            else:
#                z += roman[s[i]]
#        return z + roman[s[-1]]
#            
            
            
        
myobj = Solution()
print(myobj.romanToInt("DCXXI"))