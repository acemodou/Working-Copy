def mergeSortedArrays(arrays):
    output = []
    smallest_items = []
    for idx in range(len(arrays)):
        smallest_items.append({"row_idx": idx, "curr_pos": 0, "val": arrays[idx][0]})
    min_heap = Heap(smallest_items, MIN_HEAP)

    while not min_heap.isEmpty():
        smallest_items = min_heap.remove()
        row_idx, curr_pos, val = smallest_items["row_idx"], smallest_items["curr_pos"], smallest_items["val"]
        output.append(val)
        if curr_pos == len(arrays[row_idx])-1:
            continue
        min_heap.insert({"row_idx": row_idx, "curr_pos": curr_pos + 1, "val": arrays[row_idx][curr_pos + 1]})
    return output


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
            if j < len(array)-1 and self.compareFunc(array[j+1]["val"] , array[j]["val"]):
                j +=1
            if self.compareFunc(array[j]["val"] , array[pos]["val"]):
                array[pos], array[j] = array[j], array[pos]
                pos = j 
                j = (2 * pos) + 1
            else:
                break 
     
    def siftUp(self, array, pos):
        temp = array[pos]
        while pos > 0 and self.compareFunc(temp["val"] , array[(pos-1)//2]["val"]):
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
