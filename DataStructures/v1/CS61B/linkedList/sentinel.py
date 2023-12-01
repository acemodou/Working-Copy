class Node:
    def __init__(self, i, n=None):
        self.item = i
        self.next = n 
    

class SLList:
    def __init__(self):
        self.sentinel = Node(63, None)
        self.size = 0
    
    def addFirst(self, x):
        self.sentinel.next = Node(x, self.sentinel.next)
        self.size += 1

    def getFirst(self):
        return self.sentinel.next.item
    
    def addLast(self, x):
        ptr = self.sentinel
        self.size += 1
        while ptr.next:
            ptr = ptr.next 
        ptr.next = Node(x, None)
    
    # returns the last node in the item 
    def getLastNode(self):
        lastItem = self.sentinel

        while lastItem.next:
            lastItem = lastItem.next 
        return lastItem
    
    # return the last item 
    def getLast(self):
        lastItem = self.getLastNode()
        return lastItem.item
    
    # remove the last item in a list 
    def removeLast(self):
        deletedNode = self.getLastNode()
        if deletedNode == self.sentinel:
            return None 
        ptr = self.sentinel
        self.size -= 1
        while ptr.next != deletedNode:
            ptr = ptr.next 
        ptr.next = None 
        return deletedNode.item 

    def sizeHelper(self, ptr):
        if ptr == None:
            return 0
        return 1 + self.sizeHelper(ptr.next)
        
    def size(self):
        return self.sizeHelper(self.first)
    
    def getSize(self):
        ptr = self.first 
        totalSize = 0
        while ptr:
            ptr = ptr.next 
            totalSize += 1
        return totalSize
    
    def fastSize(self):
        return self.size
    
    def iterativeDisplay(self) -> None:
        ptr = self.sentinel.next 
        while ptr:
            print(ptr.item, end=" ")
            ptr = ptr.next
        print()

# L = SLList()
# L.addFirst(4)
# L.addFirst(10)
# L.addFirst(11)
# L.getFirst()
# L.addLast(2)
# L.iterativeDisplay()
# # print(L.size())
# print(L.fastSize())