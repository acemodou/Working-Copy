class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
        
    def addMany(self, values):
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self
        
    def getNthNode(self, n):
        counter = 1
        current = self
        while counter < n:
            current = current.next
            counter += 1
        return current
    
def findLoop(head):
    slow = head.next
    fast = head.next.next
    
    while fast != slow:
        slow = slow.next
        fast = fast.next.next
    
    slow = head
    while fast != slow:
        fast = fast.next
        slow = slow.next
    return fast
    
L = LinkedList(0)
L.addMany([1, 2, 3,4, 5, 6, 7, 8, 9])
L.getNthNode(10).next = L.getNthNode(5)
findLoop(L)