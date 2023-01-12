import unittest
import heap_construction

def isMinHeapPropertySatisfied(array):
    for i in range(1, len(array)):
        parent_idx = (i-1) //2 
        if array[parent_idx] > array[i]:
            return False 
    return True 


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        minHeap = heap_construction.Heap([48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41], heap_construction.MIN_HEAP)
        minHeap.insert(76)
        self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))
        self.assertEqual(minHeap.peek(), -5)
        self.assertEqual(minHeap.remove(), -5)
        self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))
        self.assertEqual(minHeap.peek(), 2)
        self.assertEqual(minHeap.remove(), 2)
        self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))
        self.assertEqual(minHeap.peek(), 6)
        minHeap.insert(87)
        self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))

if __name__ == "__main__":
    unittest.main()
