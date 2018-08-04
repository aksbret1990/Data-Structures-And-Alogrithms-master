# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 12:00:18 2018

@author: Akshay Jagadale
"""

class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
     
        
        ''' method 1
        perimeter = 0
        for n,row in enumerate(grid):
            #print("n: ",n)
            #print("row", row)
            for i,value in enumerate(row):
                #print("i :",i)
                #print("value: ",value)
                count1 = 0
                
                
                
                if value == 1:
                    
                    #print("for 1 at: ", n, ',' , i)
                    if n - 1 >= 0:
                        if grid[n-1][i] == 1:
                            count1+=1
                            #print("[n-1][i]")
                    else:
                          pass 
                      
                    if i+1 <= (len(row) - 1):
                        if grid[n][i+1] == 1:
                            count1+=1
                            #print("[n][i+1]")
                    else:
                          pass 
                      
                    if n+1 <= (len(grid) - 1):
                        if grid[n+1][i] == 1:
                            count1+=1  
                            #print("[n+1][i]")
                    else:
                          pass 
                      
                    if i - 1 >= 0:
                        if grid[n][i-1] == 1:
                            count1+=1 
                            #print("[n][i-1]")
                    else:
                          pass 
                        
                    #print("value: ",value,"count1 :",count1 ,"perimeter: ", 4 - count1 )    
                        
                    perimeter+= 4 - count1   
                    
                    #print()
                        
                else:
                    continue
        return perimeter
        ''' 
                   
    
    
        
myobj = Solution()

print (
       myobj.islandPerimeter([[1,1]])
    )
#
#print (
#       myobj.islandPerimeter([
#                        [0,1,0,0],
#                        [1,1,1,0],
#                        [0,1,0,0],
#                        [1,1,0,0]
#                    ])
#    )
    
    
    
    