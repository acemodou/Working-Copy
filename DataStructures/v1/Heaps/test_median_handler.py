import unittest
import median_handler
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        handler = median_handler.ContinuousMedianHandler()
        handler.insert(5)
        handler.insert(10)
        self.assertEqual(handler.getMedian(), 7.5)
        handler.insert(100)
        self.assertEqual(handler.getMedian(), 10)

if __name__ == "__main__":
    unittest.main()
