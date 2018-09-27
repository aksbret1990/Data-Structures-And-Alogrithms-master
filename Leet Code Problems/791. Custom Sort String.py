# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 14:55:03 2018

@author: Akshay Jagadale
"""

class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        
 
        final = ''
        for i in S:
            if i in T:
                for j in range(T.count(i)):
                    final += i
            
        final1 = final
        for i in T:
            if i not in final:
                final1 += i
        return(final1)
        
        
myobj = Solution()
print(myobj.customSortString('hucw',
                    "utzoampdgkalexslxoqfkdjoczajxtuhqyxvlfatmptqdsochtdzgypsfkgqwbgqbcamdqnqztaqhqanirikahtmalzqjjxtqfnh"))