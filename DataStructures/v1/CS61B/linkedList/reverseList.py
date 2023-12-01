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
    
def reverseLinkedList(head):
    # Write your code here.
    curr = head 
    prev = None 
    while curr:
        q = prev 
        prev = curr 
        curr = curr.next 
        prev.next = q
    return prev 
    


L1 = LinkedList(2)
L1.addMany([4,6,8])
reverseLinkedList(L1)