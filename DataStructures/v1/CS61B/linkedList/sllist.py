class Node:
    def __init__(self, i, n=None):
        self.item = i
        self.next = n 
    

class SLList:
    def __init__(self):
        self.first = None 
        self.size = 0
    
    def addFirst(self, x):
        self.first = Node(x, self.first)
        self.size += 1

    def getFirst(self):
        return self.first.item
    
    def addLast(self, x):
        if self.first == None:
            return self.addFirst(x)

        ptr = self.first
        self.size += 1
        while ptr.next:
            ptr = ptr.next 
        ptr.next = Node(x, None)
    
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

L = SLList()
# L.addFirst(4)
# L.addFirst(10)
# L.addFirst(11)
# L.getFirst()
L.addLast(2)
# print(L.size())
print(L.fastSize())