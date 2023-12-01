class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def addMany(self, values):
        current = self
        while current.next:
            current = current.next 
        for val in values:
            current.next = LinkedList(val)
            current = current.next 
        return self  


# This implementation fails for one case 
def removeKthNodeFromEnd(head, k):
    # Write your code here.
    kthElement = getLength(head) - k 
    current = head
    for _ in range(kthElement):
        prev = current 
        current = current.next
    
    if current == head:
        head.value = head.next.value
        head.next = head.next.next 
        return 
        
    else:
        x = prev.next.value
        prev.next = current.next
        current = None

def getLength(head):
    if head.next == None:
        return 1
    return 1 + getLength(head.next)

def removeKthNodeFromEnd(head, k):
    # Write your code here.
    fast = head 
    slow = head 
    for _ in range(k):
        fast = fast.next 
    if fast is None:
        head.value = head.next.value 
        head.next = head.next.next
        return 
    while fast.next:
        fast = fast.next
        value = slow.next.value 
        slow = slow.next
    slow.next = slow.next.next 




L = LinkedList(0)
L.addMany([1,2,3,4,5,6,7,8,9])
removeKthNodeFromEnd(L, 4)