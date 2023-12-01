import math 
class LinkedList:
    def __init__(self, val, n=None):
        self.value = val 
        self.next = n
    
    def addMany(self, values):
        current = self
        while current.next:
            current = current.next 
        for val in values:
            current.next = LinkedList(val)
            current = current.next 
        return self 

        
def removeDuplicatesFromLinkedList(linkedList):
    current = linkedList
    nextNode = linkedList.next 
    
    while nextNode:
        if current.value == nextNode.value:
            current.next = nextNode.next 
            nextNode = None 
            nextNode= current.next
        else:
            current = nextNode
            nextNode = nextNode.next
    return linkedList 

# def middleNode(LinkedList):
#     count = 0
#     current = LinkedList
#     while current:
#         count += 1
#         current = current.next
#     middleNode = LinkedList
#     for _ in range(math.floor(count // 2)):
#         middleNode = middleNode.next 
#     return middleNode

def middleNode(LinkedList):

    slow = LinkedList
    fast = LinkedList
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next 
    return slow 





L = LinkedList(1)
L.addMany([1,3,4,4,4,5,6,6])
removeDuplicatesFromLinkedList(L)
middleNode(L)