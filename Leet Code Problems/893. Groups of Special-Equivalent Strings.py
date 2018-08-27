# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 23:34:22 2018

@author: Akshay Jagadale
"""

class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        
        
        #method 1
#        def count(word):
#            array = [0] * 52
#            for i, letter in enumerate(word):
#                array[ord(letter) - ord('a') +  26 * (i%2)] += 1
#            
#            res.append(tuple(array))
#        
#        res = []
#        for word in A:
#            count(word)
#        return len(set(res))
       
        #method 2
        B = set()
        for string in A:
            C = list(string)
            a,b = C[::2], C[1::2]
            B.add((''.join(sorted(a)), ''.join(sorted(b))))
			
        return len(B)
        
        
        
mlist = ["abcd","cdab","adcb","cbad"]
myobj = Solution()
print(myobj.numSpecialEquivGroups(mlist))