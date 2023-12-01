class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def addMany(self, values):
        curr = self
        while curr.next:
            curr = curr.next
        for val in values:
            curr.next = LinkedList(val)
            curr = curr.next 
        return self

def linkedListPalindrome(head):
    # Write your code here.
    fast = head
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    reverseHead = recursive(slow)
    node = head
    revHead = reverseHead 
    while node and revHead:
        if node.value != revHead.value:
            return False 
        node = node.next
        revHead = revHead.next
    return True 

def recursive(head):
    prev = None 
    curr = None
    node = head 
    while node:
        curr = node
        node = node.next
        curr.next = prev
        prev = curr
    return prev 

L2 = LinkedList(0)
L2.addMany([1,2,2,1,0])
linkedListPalindrome(L2)