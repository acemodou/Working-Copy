import unittest
from chaining import *

class TestNode:
    def __init__(self, value):
        self.value = value 
        self.next = None 

Node = TestNode
if hasattr(chaining, "Node"):
    Node = chaining.Node 

def get_node_values_in_array(linkedlist):
    values = []
    j = 0
    while j < 10:
        while not linkedlist[j%10].isEmpty():
            values.append(linkedlist[j%10].delete())
        j += 1
    return values 

class TestProgram(unittest.TestCase):
    def test_chaining(self):
         Hash_values = [16, 12 ,25, 39 , 6, 122, 5 ,68, 75]
         linked_list = chaining(Hash_values)
         self.assertEqual(search(linked_list, 122), True)
         self.assertEqual(get_node_values_in_array(linked_list), [12, 122, 5, 25, 75, 6, 16, 68, 39])

if __name__ == "__main__":
    unittest.main()