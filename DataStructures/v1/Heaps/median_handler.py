import heap_construction
class ContinuousMedianHandler:
    def __init__(self):
        # Write your code here.
        self.median = None
        self.small_elements = heap_construction.Heap([], heap_construction.MAX_HEAP)
        self.large_elements = heap_construction.Heap([], heap_construction.MIN_HEAP)

    def insert(self, number):
        # insert elements in the max heap .
        self.small_elements.insert(number)

        # Rebalance the heap 
        self.re_balance()
        self.update_median()
    
    def re_balance(self):
        if self.small_elements.length and self.large_elements.length \
            and self.small_elements.peek() > self.large_elements.peek():
            top_value = self.small_elements.remove()
            self.large_elements.insert(top_value)
        
        if self.small_elements.length > self.large_elements.length + 1:
            top_value = self.small_elements.remove()
            self.large_elements.insert(top_value)

        if self.large_elements.length > self.small_elements.length + 1:
            top_value = self.large_elements.remove()
            self.small_elements.insert(top_value)

    def update_median(self):
        if self.small_elements.length == self.large_elements.length:
            self.median = (self.small_elements.peek() + self.large_elements.peek()) / 2 
        elif self.small_elements.length > self.large_elements.length:
            self.median = self.small_elements.peek()
        else:
            self.median = self.large_elements.peek()

    def getMedian(self):
        return self.median
