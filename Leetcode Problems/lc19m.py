"""
19. Remove Nth Node From End of List

Given a linked list, remove the n-th node from the end of list and return its head.

Example:
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:
Could you do this in one pass?
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """

    high = low = head
    while n > 0:
        high = high.next
        n -= 1
    if not high:
        return head.next
    while high.next:
        high = high.next
        low = low.next
    low.next = low.next.next
    return head


def print_ll(head):
    while head:
        print(head.val, end=' -> ')
        head = head.next
    print(None)


h = ListNode(1)
c = h
c.next = ListNode(2)
c = c.next
c.next = ListNode(3)
c = c.next

c.next = None

print_ll(h)
print()
print_ll(removeNthFromEnd(h, 3))
