# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 20:49:59 2018

@author: Akshay Jagadale
"""

class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        nums = []
        comlist = []
        comlist.append(a)
        comlist.append(b)
        for a in comlist:
            #print(a)
            i = ''
            isign = ''
            ind = 0
            
            if a[ind] != '-':
                isign = '+'
            else:
                isign = '-'
                ind += 1
            
            
            while a[ind] != '+':
                i += a[ind]
                ind+=1
                
    
            
            if isign == '-':
                i = -1 * int(i)
            else:
                i = int(i)
            
            #print(i)
            
            
            k = ''
            ksign = ''
            ind+=1
            if a[ind] != '-':
                ksign = '+'
            else:
                ksign =  '-'
                ind+=1
                
            while a[ind] != 'i':
                k += a[ind]
                ind+=1
                
            if ksign == '-':
                k = -1 * int(k)
            else:
                k = int(k)
            
            #print(k)
            
            nums.append((i,k))
            
        #print(nums)
        
        first = nums[0][0] * nums[1][0]
        second = nums[0][0] * nums[1][1]
        third = nums[0][1] * nums[1][0]
        forth = nums[0][1] * nums[1][1]
        
        
        final_first = first + (forth * -1)
        final_second = second + third
        
        #print(str(final_first) + '+' + str(final_second) + 'i')
            
        return str(final_first) + '+' + str(final_second) + 'i'
            
            
myobj = Solution()
myobj.complexNumberMultiply('1+-1i','1+-1i')