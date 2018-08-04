# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 12:57:45 2018

@author: Akshay Jagadale
"""


 #Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        #method 2 recursive
        if root == None:
            return root
        right = self.invertTree(root.right)
        left = self.invertTree(root.left)
        root.right = left
        root.left = right
        return root
        
        
        #method 1 itertive 
        '''
        if root is None:
            return root
        
        queue = []
        queue.append(root)
        while len(queue) > 0:
            node = queue.pop(0)
            node.left,node.right = node.right, node.left
            
            if node.left is not None:
                queue.append(node.left)
            
            if node.right is not None:
                queue.append(node.right)
        
        return root   
        
        '''
        

            
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

t1 = TreeNode(4)
t1.left = u1 = TreeNode(2)
t1.right = v1 = TreeNode(7)
u1.left = w = TreeNode(1)
u1.right = x = TreeNode(3)
v1.left = m = TreeNode(6)
v1.right = n = TreeNode(9)


printLevelOrder(t1)
myobj = Solution()
tres = myobj.invertTree(t1)
print("After")
printLevelOrder(tres)