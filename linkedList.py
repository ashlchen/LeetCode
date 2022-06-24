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
def reorderList(self, head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    #multiple pass
    
    # find first section and second section
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    second = slow.next
    prev = slow.next = None
    # change second section direction
    while second:
        temp = second.next
        second.next = prev
        prev = second
        second = temp
    
    cur = head
    while prev:
        temp1 = cur.next
        temp2 = prev.next
        cur.next = prev
        prev.next = temp1
        prev = temp2
        cur = temp1
        
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]: 
        dummy = ListNode()
        dummy.next = head
        # first pass to find the total length
        curLen = 0
        pointer = dummy
        while pointer.next:
            pointer = pointer.next
            curLen += 1
        # find target node counting from front
        remove_node = curLen - n
        cur = dummy
        # move cur to the node before remove_node
        for i in range(remove_node):
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next