# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 22:53:01 2018

@author: Akshay Jagadale
"""

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        
        #using sorted
#        news = sorted(s)
#        newt = sorted(t)
#        
#        for i in range(0,len(news)):
#            if news[i] != newt[i]:
#                return newt[i]
#        
#        return newt[-1]
    
        #methos2: using order and char 
        from functools import reduce
        import operator
        #return chr(reduce(operator.xor, map(ord, s + t)))
        
        #or
#        
#        code = 0
#        for ch in s + t:
#            code ^= ord(ch)
#        return chr(code)
        
        #method3: using collections
#        import collections
#        return list((collections.Counter(t) - collections.Counter(s)))[0]
        
        #method4: using dictionaries
#        dic = {}
#        for ch in s:
#            dic[ch] = dic.get(ch, 0) + 1
#        for ch in t:
#            if dic.get(ch, 0) == 0:
#                return ch
#            else:
#                dic[ch] -= 1
        
        #method 5:
#        
#        diff = 0
#        for i in range(len(s)):
#            diff -= ord(s[i])
#            diff += ord(t[i])
#        diff += ord(t[-1])
#        return chr(diff)
        
        
        
myobj = Solution()
print(myobj.findTheDifference("abcd","abcde"))