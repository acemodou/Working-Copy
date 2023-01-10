import unittest
from DFS import Graph

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        dfs = Graph()
        dfs.addEdge(0, 2)
        dfs.addEdge(0, 1)
        dfs.addEdge(1, 2)
        dfs.addEdge(2, 0)
        dfs.addEdge(2, 3)
        dfs.addEdge(3, 3)

        self.assertEqual(dfs.DFS(0), [0, 2, 3, 1])
    
if __name__ == "__main__":
    unittest.main()
