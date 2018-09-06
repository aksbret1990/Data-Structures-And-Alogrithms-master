# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 14:40:03 2018

@author: Akshay Jagadale
"""

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        #recursive preorder traversal
        if t == None:
            return ""
        if t.left == None and t.right == None:
            return str(t.val)
        if t.left != None and t.right == None:
            return str(t.val) + "(" + self.tree2str(t.left) +")"
        return str(t.val) + "(" + self.tree2str(t.left) +")" + "(" + self.tree2str(t.right) +")"

        #Iterative Method Using stack
#        if not t: return ""
#        stack = []
#        stack.append(t)
#        res = ""
#        while stack:
#            node = stack.pop()
#            if node == ")":
#                res += ")"
#                continue
#            res += "("+str(node.val)
#            if not node.left and  node.right:
#                res += "()"
#            if  node.right:
#                stack.append(")")
#                stack.append(node.right)
#            if  node.left:
#                stack.append(")")
#                stack.append(node.left)
#
#        return res[1:]       
        
        

n1 = TreeNode(1)
n1.left = n2 = TreeNode(2)
n1.right = n3 = TreeNode(3)
n2.left = n4 = TreeNode(4)

myobj = Solution()
print(myobj.tree2str(n1))
