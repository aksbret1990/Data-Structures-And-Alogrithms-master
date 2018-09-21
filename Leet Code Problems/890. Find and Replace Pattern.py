# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 10:16:39 2018

@author: Akshay Jagadale
"""

class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        
        #method: my own
#        res = []
#        for word in words:
#            flag = 1
#            #print(word)
#            visited = []
#            mapped = []
#            mdict = {}
#            for i in range(0,len(pattern)):
#                #print(i)
#                if pattern[i] not in visited and word[i] not in mapped:
#                    visited.append(pattern[i])
#                    mapped.append(word[i])
#                    mdict[pattern[i]] = word[i]
#
#                if word[i] != mdict.get(pattern[i]):
#                    flag = 0
#                    break
#                
#                elif word[i] != mdict.get(pattern[i]):
#                    continue
#                
#            if flag == 1:
#                #print(word)
#                res.append(word)
#        return res     
    
        #method: Approach 1: Two Maps
#        def match(word):
#            m1, m2 = {}, {}
#            for w, p in zip(word, pattern):
#                if w not in m1: m1[w] = p
#                if p not in m2: m2[p] = w
#                if (m1[w], m2[p]) != (p, w):
#                    return False
#            return True
#
#        return list(filter(match, words))
        
        #method: Approach 2: One Map
        def match(word):
            P = {}
            for x, y in zip(pattern, word):
                if P.setdefault(x, y) != y:
                    return False
            return len(set(P.values())) == len(P.values())

        return list(filter(match, words))
        
        
        
myobj = Solution()
print(myobj.findAndReplacePattern(["abc","cba","xyx","yxx","yyx"], "abc"))