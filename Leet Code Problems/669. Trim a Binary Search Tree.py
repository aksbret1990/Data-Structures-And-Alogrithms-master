# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 13:31:53 2018

@author: Akshay Jagadale
"""

 #Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        
        
        def trim(node):
            if node:
                if node.val > R:
                    return trim(node.left)
                elif node.val < L:
                    return trim(node.right)
                else:
                    node.left = trim(node.left)
                    node.right = trim(node.right)
                    return node

        
        return trim(root)

        
n3 = TreeNode(3)
n3.left = n0 = TreeNode(0)
n3.right = n4 = TreeNode(4)
n0.right = n2 = TreeNode(2)
n2.left = n1 = TreeNode(1)


myobj = Solution()
myobj.trimBST(n3,1,3)



