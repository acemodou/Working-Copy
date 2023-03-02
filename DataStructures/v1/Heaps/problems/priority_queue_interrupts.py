import time

class Heap:
    def __init__(self, array):
        # self.heap = self.build_heap(array)
        self.heap = self.heapify(array)
    
    def build_heap(self, array):
        for i in range(1, len(array)):
            self.swim(array, i)
        return array 
    
    def heapify(self, array):
        N = len(array)
        for i in reversed(range(N//2)):
            self._siftDown(array, i)
        return array 
    
    def _siftDown(self, array, pos):
        j = (2*pos) + 1
        endpos = len(array)
        while j < endpos:
            if j < endpos-1 and array[j+1] < array[j]:
                j +=1
            if array[j] < array[pos]:
                array[j], array[pos] = array[pos], array[j]
                pos = j 
                j = (2 * pos) + 1
            else:
                break 

    
    def swim(self, array, pos):
        temp = array[pos]
        while pos > 0 and temp[0] < array[(pos-1) // 2][0]:
            array[pos] = array[(pos-1)//2]
            pos = (pos-1) //2
        array[pos] = temp 
    
    def sink(self, pos):
        j = (2*pos) + 1
        endpos = len(self.heap)
        while j < endpos:
            if j < endpos-1 and self.heap[j+1] < self.heap[j]:
                j +=1
            if self.heap[j] < self.heap[pos]:
                self.heap[j], self.heap[pos] = self.heap[pos], self.heap[j]
                pos = j 
                j = (2 * pos) + 1
            else:
                break 

    def remove(self):
        lastit = self.heap.pop()
        if self.heap:
            returnitem = self.heap[0]
            self.heap[0] = lastit
            self.sink(0)
            return returnitem
        return lastit
    
    def insert(self, value):
        self.heap.append(value)
        self.swim(self.heap, len(self.heap)-1)
   



# Jobs to be executed 
jobs = [(2, 'task_1'), (5, 'task_2'), (1, 'task_4'),
        (4, 'task_5'), (3, 'task_3'), (1, 'task_8')]

# interrupts
interrupts = [(1, 'intr_1'), (2, 'intr_2'), (13, 'intr_3')]

# Arrange jobs into heap 
hq = Heap(jobs)

print(jobs, "\n\n")

j = 0 

# Scheduling the tasks 
while len(jobs) != 0:
    print(f"{jobs[0][1]} with priority {jobs[0][0]}, in progress", end="")
    # Servicing the task
    for _ in range(0, 5):
        print(".", end="")
        time.sleep(0.5)
    Q = hq.remove()
    print(f"\nRemoving {Q} from the Queue")
    if j < len(interrupts):
        hq.insert(interrupts[j])
        print(f"\n\n New interrupt arrived!!{interrupts[j]}")
        j +=1
