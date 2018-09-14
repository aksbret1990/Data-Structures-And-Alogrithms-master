# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 17:08:36 2018

@author: Akshay Jagadale
"""

class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """

        #method: my try
#        comdict = {}     
#        for i in list1:
#            if i in list2:
#                #print(i)
#                comdict[i] = list1.index(i) + list2.index(i)
#        #print(comdict)
#        
#        s = sorted(comdict.items(), key = lambda t: t[1])
#        #print(s[0][0])
#        #return s[0][0]
#        #print(s)
#        val = s[0][1]
#        finlist = []
#        
#        for i in range(0,len(s)):
#            if val == s[i][1]:
#                finlist.append(s[i][0])
#        #print(finlist)
#        return finlist
#            
        
        #method: fastest
        dict1 = {}
        for i in range(len(list1)):
            dict1[list1[i]] = i
        
        minIndex = float('inf')
        minPlace = []
        for i in range(len(list2)):
            if list2[i] in dict1:
                score = i + dict1[list2[i]]
                if score == minIndex:
                    minPlace.append(list2[i])
                elif score < minIndex:
                    minIndex = score
                    minPlace = [list2[i]]
                
        
        return minPlace
        
myobj = Solution()
myobj.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"], ["KFC", "Shogun", "Burger King"])