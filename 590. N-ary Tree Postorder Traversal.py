# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 13:23:10 2018

@author: Akshay Jagadale
"""


# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        
        #method 1
#        rlist = []
#        def rec(root):
#            if root:
#                if root.children:
#                    for i in root.children:
#                        rec(i)
#                    rlist.append(root.val)
#                    
#                else:
#                    rlist.append(root.val)
#     
#        rec(root)
#        return rlist

method2: Iteration is basically pre-order traversal but rather than go left, go right first then reverse its result. 
        res = []        
        stack = [root]
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            if curr.children:
                stack.extend(curr.children)

        return res[::-1]
            
        
        method 1: recursion

            
    
five = Node(5,None)
six = Node(6,None)
three  = Node(3,[five, six])
two = Node(2,None)
four = Node(4,None)
one = Node(1,[three,two,four])        


mobj = Solution()
print(mobj.postorder(one))

