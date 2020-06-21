class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def removeDuplicates(head):
    i = head
    j = head.next
    while j:
        if i.data != j.data:
            i.next = j
            i = i.next
        j = j.next
    i.next = j
    return head


def insert(head, data):
    p = Node(data)
    if not head:
        head = p
    elif not head.next:
        head.next = p
    else:
        start = head
        while start.next:
            start = start.next
        start.next = p
    return head


def display(head):
    current = head
    while current:
        print(current.data, end=' ')
        current = current.next


head = Node(None)
t = int(input())
for _ in range(t):
    insert(head, int(input()))
display(head)
removeDuplicates(head)
print()
display(head)
