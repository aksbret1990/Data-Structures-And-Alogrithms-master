# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 23:49:02 2018

@author: Akshay Jagadale
"""

class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        
        if len(word) == 1:
            return True
        
        if len(word) == 2:
            if word[0].islower() and word[1].isupper():
                return False
            else:
                return True
            
        else:
            zero = word[0].isupper()
            first = word[1].isupper()
            
            for i in range(2,len(word)):
                if zero == True and first == True:
                    if word[i].isupper() == True:
                        continue
                    else:
                        return False
                    
                if zero == False and first == False:
                     if word[i].isupper() == False:
                         continue
                     else:
                         return False
                     
                if zero == True and first == False:
                     if word[i].isupper() == False:
                         continue
                     else:
                         return False
                     
                else:
                    return False
                
            return True
                
            
    
myobj = Solution()
res = myobj.detectCapitalUse('FFFFFFFFFFFFFFFFFFFFf')
print(res)