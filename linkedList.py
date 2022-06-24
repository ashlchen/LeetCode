class Node:
    def __init__(self, val = 0, next=None):
        self.val = val
        self.next = next

def remove_element(head, target):
    dummy = Node()
    cur = dummy
    dummy.next = head
    while cur:
        if cur.next.val == target:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return dummy.next

def printList(node):
    while node:
        print(node.val, end=" ")
        node = node.next


a = Node(1)
b = Node(2)
c = Node(3)
a.next = b
b.next = c
printList(a)