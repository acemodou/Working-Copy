class ContinuousMedianHandler:
    def __init__(self):
        self.median = None
        self.smallest_elements = Heap(MAX_HEAP_FUNC, [])
        self.largest_elements = Heap(MIN_HEAP_FUNC, [])
    
    def insert(self, number):
        self.largest_elements.insert(number)
        self.reBlance()
        self.updateMedian()
    
    def reBlance(self):
            if self.largest_elements.length and self.smallest_elements.length and \
                self.smallest_elements.peek() > self.largest_elements.peek():
                    self.largest_elements.insert(self.smallest_elements.remove())

            if self.largest_elements.length > self.smallest_elements.length + 1:
                self.smallest_elements.insert(self.largest_elements.remove())
            
            if self.smallest_elements.length > self.largest_elements.length + 1:
                self.largest_elements.insert(self.smallest_elements.remove())

    def updateMedian(self):
        
        if self.largest_elements.length == self.smallest_elements.length:
            self.median = (self.largest_elements.peek() + self.smallest_elements.peek()) / 2
        
        elif self.smallest_elements.length > self.largest_elements.length:
            self.median = self.smallest_elements.peek()
        
        else:
            self.median = self.largest_elements.peek()

    def getMedian(self):
        return self.median 

class Heap:
    def __init__(self, compareFunc, array):
        self.heap = self.buildHeap(array)
        self.compareFunc = compareFunc
        self.length = len(array)
    
    def buildHeap(self, array):
        for pos in range(1, len(array)):
            self.siftUp(array, pos )
        return array

    def PARENT(self, idx):
        return (idx -1) >> 1
    
    def CHILD(self, idx):
        return (idx << 1) + 1
    
    def siftUp(self, array, pos):
        # Hold the value at pos and keep going up until there is nothing smaller than it
        temp = array[pos]
        while pos > 0 and self.compareFunc(temp, array[self.PARENT(pos)]):
            array[pos] = array[self.PARENT(pos)]  
            pos = self.PARENT(pos)
        array[pos] = temp
    
    def siftDown(self, pos):
        child = self.CHILD(pos)
        while child < len(self.heap)-1:
            if self.compareFunc(self.heap[child+1], self.heap[child]):
                child = child+1
            if self.heap[pos] > self.heap[child]:
                self.swap(pos, child, self.heap)
                pos = child 
                child = self.CHILD(pos)
            else:
                break 

    def insert(self, value):
        self.heap.append(value)
        self.length +=1
        self.siftUp(self.heap, len(self.heap)-1)
    
    def peek(self):
        return self.heap[0]

    def swap(self, x, y, heap):
        if x != y:
            heap[x], heap[y]  = heap[y], heap[x] 

    def remove(self):
        x = self.peek()
        self.swap(0, len(self.heap)-1, self.heap)
        deleted_ele = self.heap.pop()
        assert f'{x} == {deleted_ele}, {x}!{deleted_ele}'
        self.siftDown(0)
        self.length -=1
        return deleted_ele 

def MAX_HEAP_FUNC(a, b):
    return a > b

def MIN_HEAP_FUNC(a, b):
   return a < b

