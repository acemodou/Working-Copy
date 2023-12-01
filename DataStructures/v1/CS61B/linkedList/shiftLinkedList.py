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

def shiftLinkedList(head, k):
    length = 1
    currTail = head
    while currTail.next:
        length += 1
        currTail = currTail.next
    
    newLength = abs(k) % length
    if newLength == 0:
        return head 
    offSet = length - newLength if k > 0 else newLength
    
    newTail = head
    for _ in range(1, offSet):
        newTail = newTail.next
    newHead = newTail.next
    newTail.next = None 
    currTail.next = head 
    return newHead 


L2 = LinkedList(1)
L2.addMany([2,3,4,5])
shiftLinkedList(L2, -2)