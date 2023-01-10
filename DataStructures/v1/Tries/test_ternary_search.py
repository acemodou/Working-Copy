import unittest
from ternary_search import TST

class TestProgram(unittest.TestCase):
    def test_tst(self):
        tst = TST()
        tst.put("apple", 1)
        tst.put("orange", 2)

        self.assertEqual(tst.get("apple"), 1)
        self.assertEqual(tst.get("orange"), 2)


if __name__ == "__main__":
    unittest.main()
