# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                print('v1 :', v1)
                l1 = l1.next
            if l2:
                v2 = l2.val
                print('v2 :', v2)
                l2 = l2.next
            carry, val = divmod(v1+v2+carry, 10)
            print('carry :',carry)
            print('val', val)
            n.next = ListNode(val)
            n = n.next
        return root.next
    

n1 = ListNode(2)
n1.next = n2 = ListNode(4)
n3 = n2.next = ListNode(3)

n = n1 

while (n != None):
    if n.next == None:
        print (n.val,end="")
    else:
        print (n.val,'-->',end="")
    n = n.next


print()

m1 = ListNode(5)
m1.next = m2 = ListNode(6)
m3 = m2.next = ListNode(4)

n = m1 

while (n != None):
    if n.next == None:
        print (n.val,end="")
    else:
        print (n.val,'-->',end="")
    n = n.next
    
print()

myobject = Solution()
n = myobject.addTwoNumbers(n1,m1) 

while (n != None):
    if n.next == None:
        print (n.val,end="")
    else:
        print (n.val,'-->',end="")
    n = n.next






'''
print('n1 :',n1.val)
print('n2 :',n2.val)
print('n3 :',n3.val)

n = n1 

while (n != None):
    if n.next == None:
        print (n.val,end="")
    else:
        print (n.val,'-->',end="")
    n = n.next
'''

        