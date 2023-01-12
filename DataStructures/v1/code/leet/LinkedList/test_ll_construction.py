import doubly_ll_construction
import unittest

class TestNode:
    def __init__(self, value):
        self.value = value 
        self.prev  = None 
        self.next  = None 

Node = TestNode
if hasattr(doubly_ll_construction, "Node"):
    Node = doubly_ll_construction.Node

def bind(nodeOne, nodeTwo):
    nodeOne.next = nodeTwo 
    nodeTwo.prev = nodeOne 

def getNodeValuesHeadToTail(linkedList):
    node = linkedList.head  
    values = []
    while node:
        values.append(node.value)
        node = node.next 
    return values 

def getNodeValuesTailToHead(linkedList):
    node = linkedList.tail 
    values = []
    while node:
        values.append(node.value)
        node = node.prev
    return values 

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        linkedList = doubly_ll_construction.DoublyLinkedList()
        one = Node(1)
        two = Node(2)
        three = Node(3)
        three2 = Node(3)
        three3 = Node(3)
        four = Node(4)
        five = Node(5)
        six = Node(6)
        # bind(one, two)
        # bind(two, three)
        # bind(three, four)
        # bind(four, five)
        # linkedList.head = one 
        # linkedList.tail = five

        # linkedList.setHead(four)
        # self.assertEqual(getNodeValuesHeadToTail(linkedList), [4, 1, 2, 3, 5])
        # self.assertEqual(getNodeValuesTailToHead(linkedList), [5, 3, 2, 1, 4])

        # linkedList.setTail(six)
        # self.assertEqual(getNodeValuesHeadToTail(linkedList), [4, 1, 2, 3, 5, 6])
        # self.assertEqual(getNodeValuesTailToHead(linkedList), [6, 5, 3, 2, 1, 4])

        # linkedList.insertBefore(six, three)
        # self.assertEqual(getNodeValuesHeadToTail(linkedList), [4, 1, 2, 5, 3, 6])
        # self.assertEqual(getNodeValuesTailToHead(linkedList), [6, 3, 5, 2, 1, 4])

        # linkedList.insertAfter(six, three2)
        # self.assertEqual(getNodeValuesHeadToTail(linkedList), [4, 1, 2, 5, 3, 6, 3])
        # self.assertEqual(getNodeValuesTailToHead(linkedList), [3, 6, 3, 5, 2, 1, 4])

        # linkedList.insertAtPosition(1, three3)
        # self.assertEqual(getNodeValuesHeadToTail(linkedList), [3, 4, 1, 2, 5, 3, 6, 3])
        # self.assertEqual(getNodeValuesTailToHead(linkedList), [3, 6, 3, 5, 2, 1, 4, 3])

        # linkedList.removeNodesWithValue(3)
        # self.assertEqual(getNodeValuesHeadToTail(linkedList), [4, 1, 2, 5, 6])
        # self.assertEqual(getNodeValuesTailToHead(linkedList), [6, 5, 2, 1, 4])

        # linkedList.remove(two)
        # self.assertEqual(getNodeValuesHeadToTail(linkedList), [4, 1, 5, 6])
        # self.assertEqual(getNodeValuesTailToHead(linkedList), [6, 5, 1, 4])

        # self.assertEqual(linkedList.containsNodeWithValue(5), True)

if __name__ == "__main__":
    unittest.main()
        