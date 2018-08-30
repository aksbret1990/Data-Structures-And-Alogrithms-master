# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 12:53:17 2018

@author: Akshay Jagadale
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
#        count = 0
#        i = 0
#        while i < len(nums):
#            if nums[i] == 0:
#                del nums[i]
#                count += 1
#                i = 0
#                continue            
#            i += 1
#                
#        for i in range(0,count):
#                nums.append(0)
#                
#        print(nums)


#        l = len(nums)
#        i = 0
#        while i<l:
#            num = nums[i]
#            if num==0:
#                nums.append(nums.pop(i))
#                l -= 1#once poped deduct the length of sequence
#                i -= 1#once poped deduct the pointer
#            i += 1
        
        last0 =  0
        
        for i in range(0,len(nums)):
            if nums[i] != 0 :
                nums[last0], nums[i] =  nums[i], nums[last0]
                last0 += 1
                
        print(nums)



        
myobj = Solution()
myobj.moveZeroes([1,0,2,4,56,0,99,0])


