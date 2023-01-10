def simple_assert(a, b):
    assert a == b, f'{a} ! {b}'
# import heapq
# class MedianFinder(object):

#     def __init__(self):
#         self.smaller_elements = []
#         self.larger_elements = []
        
#     def addNum(self, num):
#         """
#         :type num: int
#         :rtype: None
#         """
#         heapq.heappush(self.smaller_elements, -1 *num)

#         if self.larger_elements and self.smaller_elements and \
#          -1 * self.smaller_elements[0] >  self.larger_elements[0]:
#             val = -1 * heapq.heappop(self.smaller_elements)
#             heapq.heappush(self.larger_elements, val)
        
#         if len(self.larger_elements) > len(self.smaller_elements) + 1:
#             val = heapq.heappop(self.larger_elements)
#             heapq.heappush(self.smaller_elements, -1 * val)
        
#         if len(self.smaller_elements) > len(self.larger_elements) + 1:
#             val = -1 * heapq.heappop(self.smaller_elements)
#             heapq.heappush(self.larger_elements, val)
        
#     def findMedian(self):
#         """
        
#         # :rtype: float
#         """
#         if len(self.larger_elements) > len(self.smaller_elements):
#             return self.larger_elements[0]
    
#         if len(self.smaller_elements) > len(self.larger_elements):
#             return self.smaller_elements[0]
        
#         return (-1 * self.smaller_elements[0] + self.larger_elements[0]) / 2


# # Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(3)
# obj.addNum(2)
# obj.addNum(7)
# obj.addNum(4)




# Do not edit the class below except for
# the insert method. Feel free to add new
# properties and methods to the class.
class ContinuousMedianHandler:
    def __init__(self):
        # Write your code here.
        self.median = None
        self.decreasingElements = Heap(MAX_HEAP_FUNC, [])
        self.increasingElements = Heap(MIN_HEAP_FUNC, [])

    def insert(self, number):
        self.decreasingElements.insert(number)
        self.reBlance()
        self.updateMedian()
        
    def reBlance(self):
        if self.decreasingElements.length and self.increasingElements.length and \
        self.decreasingElements.peek() > self.increasingElements.peek():
            self.increasingElements.insert(self.decreasingElements.remove())

        if self.decreasingElements.length > self.increasingElements.length+1:
            self.increasingElements.insert(self.decreasingElements.remove())
        if self.increasingElements.length > self.decreasingElements.length+1:
            self.decreasingElements.insert(self.increasingElements.remove())
        
    def updateMedian(self):

        if self.decreasingElements.length == self.increasingElements.length:
            self.median = (self.decreasingElements.peek() + self.increasingElements.peek()) / 2
        elif self.decreasingElements.length > self.increasingElements.length:
            self.median = self.decreasingElements.peek()
        else:
            self.median = self.increasingElements.peek()
        
    def getMedian(self):
        return self.median

class Heap:
    def __init__(self, compareFunc, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)
        self.compareFunc = compareFunc
        self.length = len(array)

    def buildHeap(self, array):
        # Write your code here.
        for pos in range(1, len(array)):
            self.siftUp(array, pos)
        return array

    def siftDown(self, pos):
        # Write your code here.
        child = (2 * pos) + 1
        while child < len(self.heap)-1:
            if self.compareFunc(self.heap[child+1], self.heap[child]):
                child += 1
            if self.compareFunc(self.heap[child], self.heap[pos]):
                self.heap[child], self.heap[pos] = self.heap[pos], self.heap[child]
                pos = child 
                child = (2 * pos) + 1
            else:
                break 

    def siftUp(self, array, pos):
        # Write your code here.
        temp = array[pos]
        while pos > 0 and self.compareFunc(temp , array[(pos -1) // 2]):
            array[pos] = array[(pos -1) // 2]
            pos = (pos -1) // 2
        array[pos] = temp

    def peek(self):
        # Write your code here.
        return self.heap[0]

    def remove(self):
        # Write your code here.
        x = self.peek()
        self.heap[0] = self.heap[len(self.heap)-1]
        self.heap[len(self.heap)-1] = x
        deleted_value = self.heap.pop()
        self.length -=1
        # self.heap[0] = len(self.heap)-1
        self.siftDown(0)
        return deleted_value

    def insert(self, value):
        # Write your code here.
        self.heap.append(value)
        self.length +=1
        self.siftUp(self.heap, len(self.heap)-1)
        

def MAX_HEAP_FUNC(a, b):
    return a > b
def MIN_HEAP_FUNC(a, b):
    return a < b


obj = ContinuousMedianHandler()
obj.insert(3)
obj.insert(2)
obj.insert(7)
obj.insert(4)

param_2 = obj.getMedian()
simple_assert(param_2, 3.5)