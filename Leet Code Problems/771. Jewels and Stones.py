# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 12:22:39 2018

@author: Akshay Jagadale
"""

class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """

        mylist = []
        count = 0
    
        for i in range(len(J)):
            print('i: ',i)
            mylist.append(J[i])
            
        for i in range(len(S)):
            if S[i] in mylist:
                count+=1

        print('Count: ',count)


'''
def numJewelsInStones(self, J, S):
        setJ = set(J)
        return sum(s in setJ for s in S)
'''

myobject = Solution()     
myobject.numJewelsInStones('aA','aAAbbbb')