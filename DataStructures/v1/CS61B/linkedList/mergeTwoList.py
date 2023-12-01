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


def mergeLinkedLists(headOne, headTwo):
    finalHead = None 
    currNode = None
    
    if headOne.value < headTwo.value:
        finalHead = headOne
        currNode = headOne
        headOne = headOne.next
        currNode.next = None
    else:
        finalHead = headTwo
        currNode = headTwo 
        headTwo = headTwo.next
        currNode.next = None
    
    while headOne and headTwo:
        if headOne.value < headTwo.value:
            currNode.next = headOne
            currNode = headOne
            headOne = headOne.next
            currNode.next = None
        else:
            currNode.next = headTwo 
            currNode = headTwo
            headTwo = headTwo.next
            currNode.next = None
    
    if headOne:
        currNode.next = headOne
    if headTwo:
        currNode.next = headTwo
    return finalHead 

L1 = LinkedList(2)
L1.addMany([6, 7, 8])
L2 = LinkedList(1)
L2.addMany([2,3,4,5,6,7,8,9,10])
mergeLinkedLists(L1, L2)