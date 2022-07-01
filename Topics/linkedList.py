
class Node:
    def __init__(self, val = 0, prev = None, next=None):
        self.val = val
        self.next = next
        self.prev = prev

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


def isPalindrome(root):
    # boolean
    # fast and slow
    fast, slow = root.next, root

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    # 1 > 2   <  2    >  1 >  1
    # slow fast
    #     slow           fast
    #            second  temp
    #            prev     second
    #                           
    second = slow.next
    prev = None
    while second:
        temp = second.next
        second.next = prev
        prev = second
        second = temp
    first = root
    second = prev

    while second:
        if first.val == second.val:
            first = first.next
            second = second.next
        else:
            return False
    return True


    root = Node(1)
    a = Node(2)
    b = Node(2)
    c = Node(2)
    d = Node(1)
    root.next = a
    a.next = b
    b.next = c
    c.next = d
    print(isPalindrome(root))

def rotateList(head, k):
    # find the length first
    listLen = 0
    cur = head
    while cur:
        listLen += 1
        cur = cur.next
    

def reversePair(head):
    if not head:
        return None
    dummy = Node()
    dummy.next = head.next
    if not head.next:
        return head
    cur = head
    while cur and cur.next:
        temp = cur.next
        new_section = temp.next
        if temp.next:
            connection = temp.next.next
        else:
            connection = new_section
        temp.next = cur
        cur.next = connection
        cur = new_section
    return head

def reverseDoublyList(head):
    
def testCase():