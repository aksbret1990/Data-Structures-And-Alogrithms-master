# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 14:01:15 2018

@author: Akshay Jagadale
"""

class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #method one-pass and O(M) space and using counter
#        
#        
#        
#        first = {}
#        counter = {}
#        degrees = 0
#        res = 0
#        
#        
#        for i, v in enumerate(nums):
#            first.setdefault(v,i)
#            counter[v] = counter.get(v,0) + 1
#            if counter[v] > degrees:
#                degrees = counter[v]
#                res = i - first[v] + 1
#            elif counter[v] == degrees:
#                res = min(res, i - first[v] + 1)
#        return res
        
        #Approach #1: Left and Right Index [Accepted]
#        left, right, count = {}, {}, {}
#        for i, x in enumerate(nums):
#            if x not in left: 
#                left[x] = i
#            right[x] = i
#            count[x] = count.get(x, 0) + 1
#
#        ans = len(nums)
#        degree = max(count.values())
#        for x in count:
#            if count[x] == degree:
#                ans = min(ans, right[x] - left[x] + 1)
#
#        return ans
        
        #approach fastest
        from collections import Counter
        counter = Counter(nums)
        #print(counter)
        degree = counter.most_common(1)[0][1]
        #print(degree)
        
        if degree == 1:
            return 1

        most_frequent = []
        for num, freq in counter.most_common():
            if freq == degree:
                most_frequent.append(num)
            else:
                break

        sizes = []
        for i in most_frequent:
            sizes.append(len(nums) - nums.index(i) - nums[::-1].index(i))

        return min(sizes)

            
                
        
        
        
        
myobj = Solution()
myobj.findShortestSubArray([1,2,3,2,5])
