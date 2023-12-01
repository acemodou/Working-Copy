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


def zipLinkedList(linkedList):
    # Write your code here.
    # Split the list into two 
    # reverse the second half of the list
    # Interweave the two list
    if not linkedList.next:
        return linkedList
        
    headOne = linkedList 
    headTwo = splitLinkedList(headOne)
    reverseList = reverseLinks(headTwo)
    return interWeave(headOne,reverseList)

def splitLinkedList(headOne):
    slow = headOne
    fast = headOne
    
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    headTwo = slow.next
    slow.next = None 
    return headTwo

def reverseLinks(head): 
    curr = None
    node = head 
    while node:
        prev = curr 
        curr = node
        node = node.next
        curr.next = prev
    return curr 

def interWeave(headOne, headTwo):
    linkedListOne = headOne
    linkedListTwo = headTwo 
    
    while linkedListOne and linkedListTwo:
        linkedListOneTemp = linkedListOne.next
        linkedListTwoTemp = linkedListTwo.next
        
        linkedListOne.next = linkedListTwo
        linkedListTwo.next = linkedListOneTemp
        
        linkedListOne = linkedListOneTemp
        linkedListTwo = linkedListTwoTemp
    return headOne
        
    
L2 = LinkedList(1)
L2.addMany([2,3,4,5,6])
zipLinkedList(L2)