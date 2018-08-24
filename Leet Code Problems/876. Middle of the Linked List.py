# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 11:50:09 2018

@author: Akshay Jagadale
"""

#Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        
#        #method 1
#        if head.next == None:
#            return head
#		
#        slow,fast = head, head
#        while fast.next.next != None and fast.next != None:
#            slow = slow.next
#            fast = fast.next.next
#            #print('slow: ' + str(slow.val))
#            #print('fast: ' + str(fast.val))
#            if fast.next == None:
#                return slow
#            
#        return slow.next
        
        #method 2
        
        mlist = [head]
        
        while mlist[-1].next:
            mlist.append(mlist[-1].next)
            
        return mlist[int(len(mlist)/2)]
        
a = ListNode(1)
b = a.next = ListNode(2)
c = b.next = ListNode(3)
#d = c.next = ListNode(4)
#e = d.next = ListNode(5)
#f = e.next = ListNode(6)


#i = a
#
#while i != None:
#    print(i.val)
#    i = i.next

myobj = Solution()
print(myobj.middleNode(a).val)