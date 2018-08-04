# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 14:37:33 2018

@author: Akshay Jagadale
"""

class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        return [num for num in range(left,right + 1) if '0' not in str(num) and all(num % int(digit) == 0 for digit in str(num))]
#        
#        numlist = [i+1 for i in range(left-1,right)]
#        res = []
#        for i in numlist:
#            digit_str = str(i)
#            digit_list = [int(i) for i in digit_str]
#            count = 0
#            if 0 not in digit_list:
#                for j in range(len(digit_list)):
#                    if i % digit_list[j] == 0:
#                        count+=1
#            if count == len(digit_list):
#                res.append(i)    
#        return res

        
        
#        is_divisible = lambda num: '0' not in str(num) and all(num % int(digit) == 0 for digit in str(num))
#        return list(filter(is_divisible, range(left,right+1)))
    
    
         
        
        
myobj = Solution()
res = myobj.selfDividingNumbers(1,22)
print(res)