# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 11:53:45 2018

@author: Akshay Jagadale
"""

class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #method1: sorting
        #return sorted(s) == sorted(t)
    
        #method2: hash table
        
        if len(s) != len(t):
            return False
        
        cntdict = {} 
        for i in s:
            if i in cntdict:
                cntdict[i] += 1
            else:
                cntdict[i] = 1
        #print(cntdict)
        
        for i in t:
            if i in cntdict:
                cntdict[i] -= 1
            
        return all(i == 0 for i in cntdict.values())
        
        

            
        
myobj = Solution()
print(myobj.isAnagram('anagram','nagaram'))