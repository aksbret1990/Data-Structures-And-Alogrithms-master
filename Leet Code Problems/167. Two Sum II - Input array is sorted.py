


class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        #method: binary search
#        for i in range(len(numbers)):
#            l, r = i+1, len(numbers)-1
#            tmp = target - numbers[i]
#            while l <= r:
#                mid = l + (r-l)//2
#                if numbers[mid] == tmp:
#                    return [i+1, mid+1]
#                elif numbers[mid] < tmp:
#                    l = mid+1
#                else:
#                    r = mid-1
        
        #method: two pointer
        
#        left, right = 0, len(numbers) - 1
#        while left < right:
#            s = numbers[left] + numbers[right]
#            if s < target:
#                left += 1
#            elif s > target:
#                right -= 1
#            else:
#                return (left+1, right+1)
        
        #method1
        mdict = {}
        for i in range(0,len(numbers)):
            print('i is : ',i)
            if target - numbers[i] not in mdict:
                print(target - numbers[i])
                print('if')
                
                mdict[numbers[i]] = i
            else:
                return [mdict.get(target-numbers[i]) + 1,i + 1]
            print(mdict)
            print()
            
        
        
myobj = Solution()
print(myobj.twoSum([2,3,4],6))