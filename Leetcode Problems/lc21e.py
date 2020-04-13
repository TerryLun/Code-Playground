"""
21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of
the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    head = l3 = ListNode(0)
    while l1 and l2:
        if l1.val > l2.val:
            l3.next = l2
            l2 = l2.next
        else:
            l3.next = l1
            l1 = l1.next
        l3 = l3.next
    l3.next = l1 or l2
    return head.next


def make(a):
    head = ListNode(a[0])
    cur = head
    for i in range(1, len(a)):
        cur.next = ListNode(a[i])
        cur = cur.next
    return head


def print_list(head):
    while head:
        print(head.val, end=' -> ')
        head = head.next
    print('\b\b\b\b')


a = [1, 2, 3]
b = [1, 3, 4]
l1 = make(a)
l2 = make(b)
print_list(l1)
print_list(l2)
l3 = mergeTwoLists(l1, l2)
print_list(l3)
