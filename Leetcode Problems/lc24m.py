"""
24. Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.
You may not modify the values in the list's nodes, only nodes itself may be changed.
"""


# Definition for singly-linked list
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def swapPairs(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    d = ListNode(0)
    d.next = head
    c = d
    while c.next and c.next.next:
        left = c.next
        right = c.next.next
        c.next = right
        left.next = right.next
        right.next = left
        c = left
    return d.next


def print_l(head):
    print(head.val)
    while head.next:
        head = head.next
        print(head.val)


# 0,1,2,3,n
head = ListNode(0)
c = head
c.next = ListNode(1)
c = c.next
c.next = ListNode(2)
c = c.next
c.next = ListNode(3)
c = c.next
c.next = ListNode(4)

print_l(head)
head = swapPairs(head)
print()
print_l(head)
