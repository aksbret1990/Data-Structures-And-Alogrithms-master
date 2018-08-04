# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 15:45:51 2018

@author: Akshay Jagadale
"""

class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        
        
        import string
       
        str1 = string.ascii_lowercase
        width_dict = dict(zip(str1,widths))
        
        #print(width_dict)
        
        length = 0
        line = 1
        for letter in S:
            if length < 100:
                if width_dict[letter] <= (100 - length):
                    length += width_dict[letter]
                else:
                    line+=1
                    length = 0
                    length += width_dict[letter]
            else:
                line+=1
                length = 0
                length += width_dict[letter]
        
        return [line, length]
    
        ''' method2
        def numberOfLines(self, widths, S):
            lines, width = 1, 0
            for c in S:
                w = widths[ord(c) - ord('a')]
                width += w
                if width > 100:
                    lines += 1
                    width = w
    
            return lines, width
        '''    
        
myobj = Solution()
res = myobj.numberOfLines([4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
                    "bbbcccdddaaa"
                    )
print(res)
