class LRUCache:
    def __init__(self, maxSize):
        self.maxSize = maxSize or 1
        self.cache = {}
        self.currentSize = 0 
        self.listOfMostRecent = DoublyLinkedNode()

    def insertKeyValuePair(self, key, value):
        # Write your code here.
        if key not in self.cache:
            if self.currentSize == self.maxSize:
                self.evictLastNode()
            else:
                self.currentSize += 1
            self.cache[key] = DoublyLinkedList(key, value) 
        else:
            self.replaceValue(key, value)
        self.updateMostRecent(self.cache[key])
        
    def getValueFromKey(self, key):
        # Write your code here.
        if key not in self.cache:
            return None
        self.updateMostRecent(self.cache[key])
        return self.cache[key].value

    def getMostRecentKey(self):
        # Write your code here.
        return self.listOfMostRecent.head.key
    
    def evictLastNode(self):
        toRemove = self.listOfMostRecent.tail.key
        self.listOfMostRecent.removeTail()
        del self.cache[toRemove]
        
    def replaceValue(self, key, value):
        if key not in self.cache:
            raise Exception("The provided key is not in our cache")
        self.cache[key].value = value 
    
    def updateMostRecent(self, key):
        return self.listOfMostRecent.setToHead(key)
    
    

class DoublyLinkedNode:
    def __init__(self):
        self.head = None 
        self.tail = None
    
    def setToHead(self, node):
        if self.head == node:
            return
        
        elif self.head is None:
            self.head = node
            self.tail = node 
        
        elif self.head == self.tail:
            self.tail.prev = node
            self.head = node
            self.head.next = self.tail
        
        else:
            if node == self.tail:
                self.removeTail()
            node.removeBindings()
            self.head.prev = node 
            node.next = self.head
            self.head = node 
    
    def removeTail(self):
        if self.tail is None:
            return
        if self.tail == self.head:
            self.head = None 
            self.tail = None
            return 
     
        self.tail = self.tail.prev 
        self.tail.next = None 
        
class DoublyLinkedList:
    def __init__(self, key, value):
        self.prev = None 
        self.key = key
        self.value = value 
        self.next = None
    
    def removeBindings(self):
        if self.prev:
            self.prev.next = self.next 
        if self.next:
            self.next.prev = self.prev
    
        self.next = None 
        self.prev = None 
    


lruCache =LRUCache(3)
lruCache.insertKeyValuePair("b", 2)
lruCache.insertKeyValuePair("a", 1)
lruCache.insertKeyValuePair("c", 3)
lruCache.getMostRecentKey()
lruCache.getValueFromKey("a")
lruCache.getMostRecentKey()
lruCache.insertKeyValuePair("d", 4)
lruCache.getValueFromKey("b")
lruCache.insertKeyValuePair("a", 5)
lruCache.getValueFromKey("a")