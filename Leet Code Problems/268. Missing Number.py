# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 15:54:03 2018

@author: Akshay Jagadale
"""

class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #Approach #1 Sorting [Accepted]
#        nums.sort()
#
#        # Ensure that n is at the last index
#        if nums[-1] != len(nums):
#            return len(nums)
#        # Ensure that 0 is at the first index
#        elif nums[0] != 0:
#            return 0
#
#        # If we get here, then the missing number is on the range (0, n)
#        for i in range(1, len(nums)):
#            expected_num = nums[i-1] + 1
#            if nums[i] != expected_num:
#                return expected_num
        
        #Approach #2 HashSet [Accepted]
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number
        
myobj = Solution()
print(myobj.missingNumber([0,1]))