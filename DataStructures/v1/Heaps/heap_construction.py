class Heap:
    def __init__(self, array, compareFunc):
        # Do not edit the line below.
        self.compareFunc = compareFunc
        self.heap = self.buildHeap(array)
        self.length = len(self.heap)

    def buildHeap(self, array):
        n = len(array) //2
        for i in reversed(range(n)):
            self.siftDown(i, array)
        return array 

    def siftDown(self, pos, array):
  
        j = (2 * pos) + 1
        while j < len(array):
            if j < len(array)-1 and self.compareFunc(array[j+1] , array[j]):
                j +=1
            if self.compareFunc(array[j] , array[pos]):
                array[pos], array[j] = array[j], array[pos]
                pos = j 
                j = (2 * pos) + 1
            else:
                break 
     
    def siftUp(self, array, pos):
        temp = array[pos]
        while pos > 0 and self.compareFunc(temp , array[(pos-1)//2]):
            array[pos] = array[(pos-1)//2]
            pos = (pos-1)//2
        array[pos] = temp 
        
    def peek(self):
        return self.heap[0]

    def remove(self):
        self.length -=1
        lastitem = self.heap.pop()
        if self.heap:
            returnitem  = self.heap[0]
            self.heap[0] = lastitem
            self.siftDown(0, self.heap)
            return returnitem
        return lastitem 

    def insert(self, value):
        self.heap.append(value)
        self.length +=1
        self.siftUp(self.heap, len(self.heap)-1)
    
    def isEmpty(self):
        return self.length == 0
        
def MAX_HEAP(a, b):
    return a > b 

def MIN_HEAP(a, b):
    return a < b 
