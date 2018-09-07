# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 12:29:11 2018

@author: Akshay Jagadale
"""

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        numdict = {}
        for i in nums:
            if i in numdict:
                numdict[i] +=1
            else:
                numdict[i] = 1
            
        for k,v in numdict.items():
            if v > int(len(nums)/2):
                return k
        
        #method brute force
#        majority_count = len(nums)//2
#        for num in nums:
#            count = sum(1 for elem in nums if elem == num)
#            if count > majority_count:
#                return num
#            
            
        #Approach 2: HashMap
#        import collections
#        counts = collections.Counter(nums)
#        return max(counts.keys(), key=counts.get)
        
        #Approach 3: Sorting
#        nums.sort()
#        return nums[len(nums)//2]
#        
        #Approach 6: Boyer-Moore Voting Algorithm
        
#        count = 0
#        candidate = None
#
#        for num in nums:
#            if count == 0:
#                candidate = num
#            count += (1 if num == candidate else -1)
#
#        return candidate
        
myobj = Solution()
print(myobj.majorityElement([2,2,1,1,1,2,2]))