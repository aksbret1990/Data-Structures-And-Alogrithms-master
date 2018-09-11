# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 17:41:47 2018

@author: Akshay Jagadale
"""

class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        para1 = ''
        for i in paragraph:
            if i not in punctuations:
                para1 += i
        paragraphlist = para1.split(" ") 
        mdict = {}
        for i in paragraphlist:
            i = i.lower()
            if i not in mdict:
                mdict[i] = 1
            else:
                mdict[i] += 1
                
        from collections import OrderedDict
        sdict = OrderedDict(sorted(mdict.items(), key = lambda t : t[1], reverse = True))
        
        for i in sdict:
            if i not in banned:
                 return i
            
        
myobj = Solution()
print(myobj.mostCommonWord('Bob hit a ball, the hit BALL flew far after it was hit.',["hit"]))