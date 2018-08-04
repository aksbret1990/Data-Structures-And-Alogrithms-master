# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 15:24:08 2018

@author: Akshay Jagadale
"""


class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
          
def getLeaves(root):    
    llist = []
    
    def rec(root):
        if root.left == None and root.right == None:
            #print(root.val)
            llist.append(root.val)
            #print(llist)
        
        if root.left != None:
            rec(root.left)
            
        if root.right != None:
            rec(root.right)
            
    rec(root)
    return(llist)
    

class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """

        t1 = getLeaves(root1)
        t2 = getLeaves(root2)
        return(t1 == t2)
            
r1 = TreeNode(3)

r1.left = u1 = TreeNode(5)
r1.right = v1 = TreeNode(1)
        
u1.left = w1 = TreeNode(6)
u1.right = x1 = TreeNode(2)
v1.left = y1 = TreeNode(9)
v1.right = z1 = TreeNode(8)
        
        
x1.left = a1 = TreeNode(7)
x1.right = b1 = TreeNode(4)
        


myobj = Solution()
print(myobj.leafSimilar(r1,r1))




