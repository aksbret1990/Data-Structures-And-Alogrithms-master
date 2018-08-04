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
    

def printLevelOrder(root):    
 # Create an empty queue for level order traversal
    queue = []
 
    # Enqueue Root and initialize height
    queue.append(root)
 
    while(len(queue) > 0):
        # Print front of queue and remove it from queue
        print (queue[0].val)
        node = queue.pop(0)
 
        #Enqueue left child
        if node.left is not None:
            queue.append(node.left)
 
        # Enqueue right child
        if node.right is not None:
            queue.append(node.right)
        
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

print ("Level Order Traversal of binary tree is -")
printLevelOrder(tree)
