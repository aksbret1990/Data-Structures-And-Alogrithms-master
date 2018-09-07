# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 10:27:09 2018

@author: Akshay Jagadale
"""

class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """

        
        if len(bits) == 1:
            return True
        
        end = False
        i=0
        
        while i <= len(bits) - 2:
            if bits[i] == 1 and (bits[i+1] == 0 or bits[i+1] == 1) and i != len(bits) - 2:
                end = True
                i += 2
            elif bits[i] == 0:
                end = True
                i += 1
            elif bits[i] == 1 and (bits[i+1] == 0) and i == len(bits) - 2:
                end = False
                i = i+ 1
                
        return end
    
        #Increment Pointer [Accepted]
#        i = 0
#        while i < len(bits) - 1:
#            i += bits[i] + 1
#        return i == len(bits) - 1
        
myobj  = Solution()
print(myobj.isOneBitCharacter([1, 0, 0]))