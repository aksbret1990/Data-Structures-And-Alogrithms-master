# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 07:52:53 2018

@author: Akshay Jagadale
"""




class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
       
        group = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        result = set()
        
        for word in words:
            #print('word :', word)
            val = ''
            for s in word:
                #print('s :' ,s)
                val += group[ord(s)-ord('a')]
                #print (group[ord(s)-ord('a')])
            result.add(val)
                
            
        return len(result)
    
myobj = Solution()
print(myobj.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
            