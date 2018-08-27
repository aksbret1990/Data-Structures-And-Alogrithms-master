# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 00:19:41 2018

@author: Akshay Jagadale
"""


# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
        
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        
        #bfs
        if not root :
            return 0
        
        if root and not root.children:
            return 1
        
        max_depth = 0
        
        q = [root,'x']
        
        while len(q) > 0:
            ele = q.pop(0)
            if ele ==  'x':
                max_depth += 1
                if len(q):
                    q.append('x')
                continue
            if ele.children:
                for i in ele.children:
                    q.append(i)
                    
        return max_depth
        
##dfs
#class Solution(object):
#    def maxDepth(self, root):
#        if not root: return 0
#        if not root.children: return 1
#        return max(self.maxDepth(node) for node in root.children) + 1
    
    
    
five = Node(5,None)
six = Node(6,None)
three  = Node(3,[five, six])
two = Node(2,None)
four = Node(4,None)
one = Node(1,[three,two,four])        


mobj = Solution()
print(mobj.maxDepth(one))

