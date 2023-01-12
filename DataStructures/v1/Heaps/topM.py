class Heap:
    def __init__(self, array):
        self.N = 0
        self.heap = self.buildHeap(array)
    
    def buildHeap(self, array):
        for i in range(len(array)):
            self.swim(array , i)
            self.N += 1
        return array 
    
    def swim(self, array, pos):
        temp = array[pos]
        while pos > 0 and float(temp[-1]) < float(array[(pos-1)//2][-1]):
            array[pos] = array[(pos-1)//2]
            pos = (pos-1)//2 
        array[pos] = temp
    
    def sink(self, pos):
        j = (2 * pos) + 1
        end_pos = len(self.heap)
        while j < end_pos:
            if j < end_pos-1 and float(self.heap[j+1][-1]) < float(self.heap[j][-1]):
                j +=1 
            if float(self.heap[pos][-1]) > float(self.heap[j][-1]):
                self.heap[pos], self.heap[j] = self.heap[j], self.heap[pos]
                pos = j 
                j = (2 * pos) + 1
            else:
                break 

    def isEmpty(self):
        return self.N == 0
    
    def size(self):
        return self.N
    
    def remove_top_priority(self):
        lastit = self.heap.pop()
        self.N -= 1 
        if self.heap:
            returnitem = self.heap[0]
            self.heap[0] = lastit
            self.sink(0)
            return returnitem
        return lastit  
    
    def insert(self, value):
        self.heap.append(value)
        self.swim(self.heap, len(self.heap)-1)
        self.N += 1 

if __name__ =="__main__":
    import sys
    import os  
    batch  = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tinyBatch.txt')
    # M = sys.argv[1]
    with open(batch, 'r') as f:
        content =f.readlines()
    current_value = content[0]
    data =current_value.split()
    array = []
    array.append(data)
    pq = Heap(array)
    for values in content[1:]:
        x =values.split()

        pq.insert(x)
        if pq.size() > 5:
            pq.remove_top_priority()

    # Put all the elements in our stack
    stk = []
    while not pq.isEmpty():
        stk.append(pq.remove_top_priority())
    
    for i in reversed(range(len(stk))):
        print(f"{stk[i][0].ljust(10)}  {stk[i][1]} {stk[i][2].rjust(10)}")
