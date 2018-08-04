# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 12:30:17 2018

@author: Akshay Jagadale
"""

 #Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        
        if(t1 == None):
            return t2
        if(t2 == None):
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left,t2.left)
        t1.right = self.mergeTrees(t1.right,t2.right)
        return t1
        
        
 
# Function to  print level order traversal of tree
def printLevelOrder(root):
    h = height(root)
    for i in range(1, h+1):
        printGivenLevel(root, i)
 
 
# Print nodes at a given level
def printGivenLevel(root , level):
    if root is None:
        return
    if level == 1:
        print (root.val),
    elif level > 1 :
        printGivenLevel(root.left , level-1)
        printGivenLevel(root.right , level-1)
 
 
""" Compute the height of a tree--the number of nodes
    along the longest path from the root node down to
    the farthest leaf node
"""
def height(node):
    if node is None:
        return 0
    else :
        # Compute the height of each subtree 
        lheight = height(node.left)
        rheight = height(node.right)
 
        #Use the larger one
        if lheight > rheight :
            return lheight+1
        else:
            return rheight+1
        
t1 = TreeNode(1)
t1.left = u1 = TreeNode(3)
t1.right = v1 = TreeNode(2)
u1.left = w = TreeNode(5)


t2 = TreeNode(2)
t2.left = x2 = TreeNode(1)
t2.right = y2 = TreeNode(3)
x2.right = z2 = TreeNode(4)
y2.right = a2 = TreeNode(7)
        
myobj = Solution()
tree = myobj.mergeTrees(t1,t2)
printLevelOrder(tree)        