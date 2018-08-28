# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 14:52:27 2018

@author: Akshay Jagadale
"""

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        
               

        
        #method1: BFS traversal
#        if root is None:
#            return []
#        
#        q = []
#        q.append(root)
#        
#        while q:
#            node = q.pop(0)
#            if node.val == val:
#                return node
#            if node.left != None:
#                q.append(node.left)
#            if node.right != None:
#                q.append(node.right)
        
        
        #method 2: traverse based on greater than or lesser than value
        
        def search(node, val):
            
            if node == None:
                return None
            
            if node.val == val:
                return node
            elif node.val < val:
                return search(node.right, val)
            else:
                return search(node.left, val)
                
        return search(root, val)

        
        
            
                
        
        
one = TreeNode(1)
three = TreeNode(3)
two = TreeNode(2)
two.left = one
two.right = three
seven = TreeNode(7)
four = TreeNode(4)
four.left = two
four.right = seven

myobj = Solution()
myobj.searchBST(four,2)