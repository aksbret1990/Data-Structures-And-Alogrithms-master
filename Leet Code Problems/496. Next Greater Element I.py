# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 10:16:49 2018

@author: Akshay Jagadale
"""

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        newlist = []
        for i in range(len(nums1)):
            num = nums1[i]
            index = nums2.index(num)
            if index == (len(nums2) - 1) and i == (len(nums1)-1) :
                newlist.append(-1)
                break
            if index == (len(nums2) - 1) and i < (len(nums1)-1) :
                newlist.append(-1)
                continue
            for j in range(index+1,len(nums2)):
                if j == (len(nums2) - 1) and num >= nums2[j]:
                    newlist.append(-1)
                    break
                    
                elif num < nums2[j]:
                    newlist.append(nums2[j])
                    break
                    
                elif  j != (len(nums2)-1) and nums1[i] >= nums2[j]:
                    continue
                
        return newlist
        
    
#        cache, st = {}, []
#        for x in nums2:
#            if len(st) == 0:
#                st.append(x)
#            elif x <= st[-1]:
#                st.append(x)
#            else:
#                while st and st[-1] < x:
#                    cache[st.pop()] = x
#                st.append(x)
#        result = []
#        for x in nums1:
#            if x in cache:
#                result.append(cache[x])
#            else:
#                result.append(-1)
#        return result    

        
myobj = Solution()
res = myobj.nextGreaterElement([2,4],[1,2,3,4])
print(res)