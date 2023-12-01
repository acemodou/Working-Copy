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


def removeDuplicatesFromLinkedList(linkedList):
    """
    This removes the duplicates in place 
    """
    currPtr = linkedList
    nextPtr = linkedList.next 
    while currPtr.next and nextPtr:
        if currPtr.value != nextPtr.value:
            currPtr.next = nextPtr
            currPtr = nextPtr
            nextPtr = nextPtr.next 
        else:
            nextPtr = nextPtr.next
    
    currPtr.next = nextPtr
    return linkedList

def middleNode(linkedList):
    "This return the second half of the linkedlist "
    slowPtr = fastPtr = linkedList
    while fastPtr and fastPtr.next:
        slowPtr = slowPtr.next 
        fastPtr = fastPtr.next.next
   
    return slowPtr



L = LinkedList(1)
L.addMany([1, 3, 4, 4, 4, 5, 6, 6])
# removeDuplicatesFromLinkedList(L)
middleNode(L)





