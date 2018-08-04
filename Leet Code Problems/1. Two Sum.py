class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        d = {}
        for i,value in enumerate(nums):
            m = target - value
            if(m in d):
                return(d[m], i)
            else:
d[value] = i