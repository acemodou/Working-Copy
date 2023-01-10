import unittest
import sort_k_sorted


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [3, 2, 1, 5, 4, 7, 6, 5]
        k = 3
        expected = [1, 2, 3, 4, 5, 5, 6, 7]
        actual = sort_k_sorted.sortKSortedArray(input, k)
        self.assertEqual(actual, expected)


if __name__=="__main__":
    unittest.main()
