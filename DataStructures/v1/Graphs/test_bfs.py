import unittest
from BFS import Graph

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        bfs = Graph()
        bfs.addEdge(0, 2)
        bfs.addEdge(0, 1)
        bfs.addEdge(1, 2)
        bfs.addEdge(2, 0)
        bfs.addEdge(2, 3)
        bfs.addEdge(3, 3)

        self.assertEqual(bfs.BFS(2), [2, 0, 3, 1])
    

       
    
    

if __name__ == "__main__":
    unittest.main()
        
