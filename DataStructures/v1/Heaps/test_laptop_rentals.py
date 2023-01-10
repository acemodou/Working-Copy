import unittest
import laptop_rentals 


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [[0, 2], [1, 4], [4, 6], [0, 4], [7, 8], [9, 11], [3, 10]]
        expected = 3
        actual = laptop_rentals.laptopRentals(input)
        self.assertEqual(actual, expected)


if __name__=="__main__":
    unittest.main()
