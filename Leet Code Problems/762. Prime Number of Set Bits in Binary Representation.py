# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 13:29:51 2018

@author: Akshay Jagadale
"""


class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
  
        #method 1
#        count = 0 
#        
#        def isPrime(num):
#            if num == 1:
#                return False
#            for i in range(2,int(pow(num,0.5))+1):
#                if num % i == 0:
#                    print('not prime')
#                    return False
#            print('prime')
#            print()
#            return True

#        for i in range(L,R+1):
#            print('i: ' ,i)
#            binnum = bin(i)
#            print('binum: ', binnum)
#            num = str(binnum).count('1')
#            print('num: ', num)
#            if isPrime(num) == True:
#                count += 1
#            else:
#                continue
#        
#        return count
        
        #method 2

        #maximum number of bits for the 10**6 number is 20 so we consideer prime numbers till 19
        prime_list = [2,3,5,7,11,13,17,19]
        count = 0
        for i in range(L,R+1):
            if (str(bin(i))).count('1') in prime_list:
                count += 1
        return count
            
          
        
        
        
myobj = Solution()
res = myobj.countPrimeSetBits(244,269)
print(res)