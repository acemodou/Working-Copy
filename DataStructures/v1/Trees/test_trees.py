import trees_adt
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        program = trees_adt.Tree()
        program.create_tree()

if __name__=="__main__":
    unittest.main()