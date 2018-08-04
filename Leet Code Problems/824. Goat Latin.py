# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 01:26:47 2018

@author: Akshay Jagadale
"""

class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        Slist =  S.split()
        Rlist = []
    
        for i in range(len(Slist)):
            word = Slist[i] 
       
            if word[0].lower() in 'aeiou':
                newword = word + 'ma'
                
            else:
                newword = word[1:] + word[0] + 'ma'
                
            newword = newword + 'a' * (i+1)
            Rlist.append(newword)
            
        return " ".join(Rlist)
            
        
        
myobj = Solution()
print(myobj.toGoatLatin("The quick brown fox jumped over the lazy dog"))