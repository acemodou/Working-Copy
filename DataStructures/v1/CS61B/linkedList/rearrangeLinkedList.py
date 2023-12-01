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

def rearrangeLinkedList(head, k):
    smallHead = None 
    smallTail = None
    equalHead = None 
    equalTail = None
    bigHead = None 
    bigTail = None
    
    node = head 
    while node:
        if node.value < k:
            smallHead, smallTail = growLinkedList(smallHead, smallTail, node)
        elif node.value > k:
            bigHead, bigTail = growLinkedList(bigHead, bigTail, node)
        else:
            equalHead, equalTail = growLinkedList(equalHead, equalTail, node)
        
        prev = node
        node = node.next
        prev.next = None 
    
    firstHead, firstTail = connectLinkedList(smallHead, smallTail, equalHead, equalTail)
    finalHead, _ = connectLinkedList(firstHead, firstTail, bigHead, bigTail)
    return finalHead 

def growLinkedList(head, tail, node):
    newHead = head
    newTail = node
    
    if newHead is None:
        newHead = node 
    
    if tail is not None:
        tail.next = newTail
    
    return (newHead, newTail)
        
def connectLinkedList(headOne, tailOne, headTwo, tailTwo):
    newHead = headTwo if headOne is None else headOne
    newTail = tailOne if tailTwo is None else tailTwo 
    
    if tailOne is not None:
        tailOne.next = headTwo
    return(newHead, newTail)

L2 = LinkedList(3)
L2.addMany([0,5,2,1,4])
rearrangeLinkedList(L2, 3)