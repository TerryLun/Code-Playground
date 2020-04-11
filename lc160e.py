"""
160. Intersection of Two Linked Lists

Write a program to find the node at which the intersection of two singly linked lists begins.

Notes:
If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def getIntersectionNode(headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """
    pa = headA
    pb = headB
    while pa is not pb:
        pa = pa.next if pa else headB
        pb = pb.next if pb else headA
    return pa

#264
#15
a = ListNode(2)
heada = a
a.next = ListNode(6)
a = a.next
a.next = ListNode(4)
a = a.next
a.next = ListNode(6)

b = ListNode(1)
headb = b
b.next = ListNode(5)
b = b.next
b.next = a.next

print(getIntersectionNode(heada, headb))
