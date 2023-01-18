import merge_sorted_arrays
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        arrays = [
            [1, 5, 9, 21],
            [-1, 0],
            [-124, 81, 121],
            [3, 6, 12, 20, 150],
        ]
        output = merge_sorted_arrays.mergeSortedArrays(arrays)
        self.assertEqual(output, [-124, -1, 0, 1, 3, 5, 6, 9, 12, 20, 21, 81, 121, 150])



if __name__ == "__main__":
    unittest.main()