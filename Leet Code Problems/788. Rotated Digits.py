# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 12:40:40 2018

@author: Akshay Jagadale
"""

class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        
#        count =  0
#        for i in range(0,N+1):
#            stri = str(i)
#            newi = ''
#            good = 1
#            print('i is: ' + str(i))
#            while(stri and good == 1):
#                units = int(stri[0])
#                print('units is: ' + str(units))
#                if units in [0,1,8]:
#                    newunits  = units
#                elif units == 2:
#                    newunits = 5
#                elif units == 5:
#                    newunits = 2
#                elif units == 6:
#                    newunits = 9
#                elif units == 9:
#                    newunits = 6
#                else:
#                    good = 0
#                print('newunits is: ' + str(newunits))
#                newi += str(newunits)
#                stri = stri[1:]
#            if good == 1:
#                print('newi: ' + newi )
#                if i != int(newi):
#                    count+=1            
#                print('count is: ' + str(count))
#            print()
#            
#        return count
    
        counts = 0
        for num in range(1, N+1):
            number = str(num)
            if '3' in number or '7' in number or '4' in number: # This will be an invalid number upon rotation
                continue # Skip this number and go to next iteration
            if '2' in number or '5' in number or '6' in number or '9' in number:
                counts += 1
        return counts
                
            
                
                
        
myobj = Solution()
myobj.rotatedDigits(10)