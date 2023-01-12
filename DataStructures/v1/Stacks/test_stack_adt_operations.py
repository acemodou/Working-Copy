import unittest
from stack_adt_using_arrays import STACK
from stack_adt_linkedlist import STACKLIST


class TestProgram(unittest.TestCase):
    # def test_case_1(self):
    #     stack = STACK(5)
    #     stack.initialize()
    #     stack.Push(5)
    #     stack.Push(10)
    #     stack.Push(8)
    #     stack.Push(20)
    #     self.assertEqual(stack.Display(), [5, 10, 8, 20, 0])
    #     self.assertEqual(stack.Pop(), 20)
    #     self.assertEqual(stack.Peek(1), 8)
    #     self.assertEqual(stack.stackTop(), 8)
    
    def test_case_2(self):
        stack = STACKLIST()
        stack.push(5)
        stack.push(10)
        stack.push(8)
        stack.push(20)
        self.assertEqual(stack.display(), [20, 8, 10, 5])
        self.assertEqual(stack.pop(), 20)
        self.assertEqual(stack.pop(), 8)
        self.assertEqual(stack.pop(), 10)
        self.assertEqual(stack.pop(), 5)

if __name__=="__main__":
    unittest.main()