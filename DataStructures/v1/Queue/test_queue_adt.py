import unittest
from queue_adt_array import Queue
from circular_queue import CircularQueue
from queue_adt_linkedlist import QueueLIST


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        q = Queue(5)
        q.Enqueue(5)
        q.Enqueue(10)
        q.Enqueue(8)
        q.Enqueue(20)
        self.assertEqual(q.display(), [5, 10, 8, 20])
        self.assertEqual(q.Dequeue(), 5)
        self.assertEqual(q.display(), [10, 8, 20])
        self.assertEqual(q.peek(), 10)
        self.assertEqual(q.peek_rear(), 20)
    
    def test_case_2(self):
        q = CircularQueue(5)
        q.Enqueue(5)
        q.Enqueue(10)
        q.Enqueue(8)
        q.Enqueue(20)
        self.assertEqual(q.display(), [5, 10, 8, 20])
        self.assertEqual(q.Dequeue(), 5)
        self.assertEqual(q.display(), [10, 8, 20])
        self.assertEqual(q.peek(), 10)
        self.assertEqual(q.peek_rear(), 20)
    
    def test_case_3(self):
        q = QueueLIST()
        q.Enqueue(5)
        q.Enqueue(10)
        q.Enqueue(8)
        q.Enqueue(20)
        self.assertEqual(q.display(), [5, 10, 8, 20])
        self.assertEqual(q.Dequeue(), 5)
        self.assertEqual(q.display(), [10, 8, 20])
        self.assertEqual(q.peek(), 10)
        self.assertEqual(q.peek_rear(), 20)
        self.assertEqual(q.isFull(), False)


if __name__=="__main__":
    unittest.main()