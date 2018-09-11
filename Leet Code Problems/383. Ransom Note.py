# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 15:16:34 2018

@author: Akshay Jagadale
"""

class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        #method 1
#        ransomNotelist = list(ransomNote)
#        magazinelist = list(magazine)
#
#        for i in ransomNotelist:
#            #print(i)
#            if i not in magazinelist:
#                return False
#            magazinelist.remove(i)
#        return True
        
#        #method 2: using collections
#        from collections import Counter
#        return not (Counter(ransomNote) - Counter(magazine))
    
        #method 3 using set, count
        for i in set(ransomNote):
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True
        
myobj = Solution()
print(myobj.canConstruct("aaa", "abb"))