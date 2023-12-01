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

def nodeSwap(head):
    # Write your code here.
    temp = LinkedList(-1)
    temp.next = head
    prev = temp
    
    while prev.next and prev.next.next:
        fast = prev.next.next
        slow = prev.next 
        
        slow.next = fast.next 
        fast.next = slow 
        prev.next = fast 
        
        prev = slow
        
    return temp.next 

L = LinkedList(0)
L.addMany([1,2])
nodeSwap(L)
