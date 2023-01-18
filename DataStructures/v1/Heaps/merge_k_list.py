import heapq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __eq__(self, other):
        if self.val != other.val:
            return False
        if self.next != other.next:
            return False
        return True
        
def mergeKLists(lists):
    dummy = ListNode()
    current = dummy
    heap = []
    # Add the head of each list to the heap
    for i, head in enumerate(lists):
        if head is not None:
            heap.append((head.val, i))
    heapq.heapify(heap)

    while heap:
        val, i = heapq.heappop(heap)
        current.next = lists[i]
        current = current.next
        lists[i] = lists[i].next
        if lists[i] is not None:
            heapq.heappush(heap, (lists[i].val, i))

    return dummy.next

import unittest

class TestMergeKLists(unittest.TestCase):
    def test_mergeKLists(self):
        # Test case 1: merge 2 lists
        list1 = ListNode(1, ListNode(4, ListNode(5)))
        list2 = ListNode(1, ListNode(3, ListNode(4)))
        expected = ListNode(1, ListNode(1, ListNode(3, ListNode(4, ListNode(4, ListNode(5))))))
        self.assertEqual(mergeKLists([list1, list2]), expected)

        # Test case 2: merge 3 lists
        list1 = ListNode(1, ListNode(4, ListNode(5)))
        list2 = ListNode(1, ListNode(3, ListNode(4)))
        list3 = ListNode(2, ListNode(6))
        expected = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4, ListNode(5, ListNode(6))))))))
        self.assertEqual(mergeKLists([list1, list2, list3]), expected)

        # Test case 3: merge empty lists
        self.assertEqual(mergeKLists([]), None)

        # Test case 4: merge one list
        list1 = ListNode(1, ListNode(4, ListNode(5)))
        expected = ListNode(1, ListNode(4, ListNode(5)))
        self.assertEqual(mergeKLists([list1]), expected)


if __name__ == '__main__':
    unittest.main()
