# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 19:44:11 2018

@author: Akshay Jagadale
"""

#Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
              
        print(root.val)
        def max_depth(root):
            if root == None:
                return 0
            
            else:
                ldepth = max_depth(root.left)
                rdepth = max_depth(root.right)
                
                if ldepth > rdepth:
                    return ldepth + 1
                else:
                    return rdepth + 1
            
                
        depth = max_depth(root)
        return depth
        
        
        
n3 = TreeNode(3)
n3.left = n9 = TreeNode(9)
n3.right = n20 = TreeNode(20)
n20.left = n15 = TreeNode(15)
n20.right = n7 = TreeNode(7)
         
myobj = Solution()
res = myobj.maxDepth(n3)
print(res)
        
        
