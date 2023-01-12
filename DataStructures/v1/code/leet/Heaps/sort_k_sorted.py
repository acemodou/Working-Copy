def sortKSortedArray(array, k):
    
    minHeapWithKElements = MinHeap(array[: min(k+1, len(array))])
    sortedIdx = 0
    for idx in range(k+1, len(array)):
        array[sortedIdx] = minHeapWithKElements.remove()
        sortedIdx +=1
        minHeapWithKElements.insert(array[idx])
    
    while not minHeapWithKElements.isEmpty():
        array[sortedIdx] = minHeapWithKElements.remove()
        sortedIdx +=1
        
    return array
    
class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)
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
        while pos > 0 and temp < array[self.PARENT(pos)]:
            array[pos] = array[self.PARENT(pos)]  
            pos = self.PARENT(pos)
        array[pos] = temp
    
    def siftDown(self, pos):
        child = self.CHILD(pos)
        while child <= len(self.heap)-1:
            if len(self.heap)-1 > child and self.heap[child+1] < self.heap[child]:
                child = child+1
            if self.heap[pos] > self.heap[child]:
                self.swap(pos, child, self.heap)
                pos = child 
                child = self.CHILD(pos)
            else:
                break 
    
    def isEmpty(self):
        return len(self.heap) == 0
        
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
        self.length -=1
        self.siftDown(0)
        
        return deleted_ele 
        