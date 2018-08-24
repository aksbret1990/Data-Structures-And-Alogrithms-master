# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 14:01:34 2018

@author: Akshay Jagadale
"""

class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        
        lista = A.split(" ")
        listb = B.split(" ")
        seta = set(lista)
        setb = set(listb)
        symdiff = (list(seta.symmetric_difference(setb)))
        
        rlist = []
        for i in range(0,len(symdiff)):
            if symdiff[i] in lista:
                if lista.count(symdiff[i]) == 1:
                    rlist.append(symdiff[i])
            if symdiff[i] in listb:   
                if listb.count(symdiff[i]) == 1:
                    rlist.append(symdiff[i])

        return rlist

A = 'mqk g g' 
B = "uuz rk uuz"

myobj = Solution()
print(myobj.uncommonFromSentences(A,B))

