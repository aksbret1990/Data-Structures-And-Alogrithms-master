# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 12:42:20 2018

@author: Akshay Jagadale
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#        
        #method1
#        mylist = []
#        count = 0
#        
        for i in range(0,len(nums)):
            if nums[i] == 1:
                count += 1
            if nums[i]!= 1:
                mylist.append(count)
                count = 0
            if i == len(nums) - 1:
                mylist.append(count)
                                    
        return max(mylist)
        
#        # method 2
#        cnt = 0
#        ans = 0
#        for num in nums:
#            if num == 1:
#                cnt += 1
#                ans = max(ans, cnt)
#            else:
#                cnt = 0
#        return ans
        
        #method 3
#        n = 0
#        maxn = 0
#        for i,v in enumerate(nums):
#            if v == 1:
#                n += 1
#            else:
#                maxn = max(maxn, n)
#                n = 0
#        maxn = max(maxn, n)
#        return maxn
    
        #method 4
        
#        num_str = ''.join(map(str,nums))
#        num_list = num_str.split('0')
#        return len(max(num_list))
        
        #method 5
            #return len(max(''.join(map(str, nums)).split('0'), key=len))
        
        
myobj = Solution()
res = myobj.findMaxConsecutiveOnes([1,1,0,1,1,1])
print(res)