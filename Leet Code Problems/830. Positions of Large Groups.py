# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 15:18:03 2018

@author: Akshay Jagadale
"""

class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        
        #method : 2 pointer
        
        now=0
        lst=[]
        lstn=[]
        length=len(S)
        count=1
        
        
       
        for i in range(1,length):
            if S[i]==S[now]:
                count+=1
            else:
                if count>=3:
                    lst=[now,now+count-1]
                    lstn.append(lst)
                lst=[]    
                now=i
                count=1
        if count>=3:
            lst=[now,now+count-1]
            lstn.append(lst)
        return lstn
        
        
        
        
        #own method 1 pointer .....little complex
#        i = 0 
#        res = []
#        while i < len(S):
#            start_index = i
#            letter = S[i]
#            count = 1
#            whileflag = 'no'
#            while i!= len(S)-1 and  S[i+1] == letter:
#                whileflag == 'yes'
#                count += 1
#                i += 1
#            if whileflag == 'no':
#                last_index = i 
#            else:
#                last_index = i - 1
#            if count >= 3:
#                res.append([start_index, last_index])
#                continue
#            i += 1
#        return res
                
                
        
myobj = Solution()
print(myobj.largeGroupPositions('abc'))