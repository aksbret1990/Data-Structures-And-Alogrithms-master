# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 15:39:48 2018

@author: Akshay Jagadale
"""

class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
#        from collections import OrderedDict
#        
#        mdict = {}
#        odict = OrderedDict(mdict)
#        
#        for i in range(0,len(s)):
#            if s[i] not in odict:
#                odict[s[i]] = 1
#            else:
#                odict[s[i]] += 1
#                
#        #print(odict)
#        
#        for k,v in odict.items():
#            #print(k,v)
#            #print()
#            if v == 1:
#                return s.index(k)
#            
#        return -1
    
        #method 2
#        for i in range(len(s)):
#            c = s[i]
#            if s.count(c)==1:
#                return i
#        return -1
        
        #method 3: using collections
#        from collections import Counter
#        sc = Counter(s)
#        #print(sc)
#        for i in range(len(s)):
#            c = s[i]
#            if sc.get(c)==1:
#                return i
#
#        return -1
    
    
        #best solution on leetcode
        import string
        
        min_idx = float('inf')
        flag = True
        for ch in string.ascii_lowercase:
            l, r = s.find(ch), s.rfind(ch)
            if l != -1 and l == r and l < min_idx:
                min_idx = l
                flag = False
                
        if flag:
            return -1
        return min_idx
    

                
        
myobj = Solution()
print(myobj.firstUniqChar('dddccdbba'))