
import continuous_median
import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        handler = continuous_median.ContinuousMedianHandler()
        handler.insert(5)
        handler.insert(10)
        self.assertEqual(handler.getMedian(), 7.5)
        handler.insert(100)
        self.assertEqual(handler.getMedian(), 10)