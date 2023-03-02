from heapq import heappush, heappop

def simple_assert(a:int, b:int):
    assert a == b, f'{a}!{b}'

class MedianFinder:

    def __init__(self):
        self.largerHeap =  []
        self.smallerHeap = []
        self.median = None 
         
    def addNum(self, num: int) -> None:
        heappush(self.smallerHeap, num * -1)
        self.reBalance()
        self.updateMedian()
    
    def reBalance(self):
        if self.smallerHeap and self.largerHeap and self.smallerHeap[0] * -1 >= self.largerHeap[0]:
            val = heappop(self.smallerHeap)
            heappush(self.largerHeap, val *-1)
        if  len(self.smallerHeap) > len(self.largerHeap) + 1:
            val = heappop(self.smallerHeap)
            heappush(self.largerHeap, val *-1)
        
        if len(self.largerHeap) > len(self.smallerHeap) + 1:
            val = heappop(self.largerHeap)
            heappush(self.smallerHeap, val *-1)
    
    def updateMedian(self):
        if len(self.largerHeap) == len(self.smallerHeap):
            self.median = (self.largerHeap[0] + self.smallerHeap[0] *-1) / 2
        elif len(self.largerHeap) < len(self.smallerHeap):
            self.median = self.smallerHeap[0] * -1
        else:
            self.median = self.largerHeap[0]

    def findMedian(self) -> float:
        return self.median 
        

# Your MedianFinder object will be instantiated and called as such:
handler = MedianFinder()
handler.addNum(5)
handler.addNum(10)
simple_assert(handler.findMedian(), 7.5)
handler.addNum(100)
simple_assert(handler.findMedian(), 10)
