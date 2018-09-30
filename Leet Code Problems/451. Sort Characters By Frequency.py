# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 10:41:46 2018

@author: Akshay Jagadale
"""

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        

        
        from collections import Counter
        
        x = Counter(s)
        #print(x.most_common())
        mc = x.most_common()      

        res = ''
        for i,k in mc:
            res += i * k
            
        return(res)
                
            
        
        
myobj = Solution()
print(myobj.frequencySort('Aabb'))