from typing import List 

def simple_assert(a, b):
    assert a == b, f'{a}!{b}'

# O(v^2) time | O(v)
def depth_first_search_adj_matrix(adjacency_matrix : List[List[int]]) -> List[int]:
    visited = [0] * len(adjacency_matrix[0])
    res = dfs(adjacency_matrix, 1, visited, res=[])
    return res 

def dfs(matrix, start_idx, visited, res) -> List[int]:
    if visited[start_idx] == 0:
        res.append(start_idx)
        visited[start_idx] = 1
        for v in range(1, len(matrix[0])):
            if matrix[start_idx][v] == 1 and visited[v] == 0:
                dfs(matrix, v, visited, res)
    return res 
    
     




adjacency_matrix = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0]]


actual = [1, 2, 3, 4, 5, 6, 7]
expected = depth_first_search_adj_matrix(adjacency_matrix)
simple_assert(actual, expected)


class Node:
    def __init__(self, name : str) -> None:
        self.name = name 
        self.child = [] 
    
    def add_child(self, child_node : 'Node') -> 'Node':
        self.child.append(Node(child_node))
        return self 
    
    def depth_first_search_adj_list(self, res):
        res.append(self.name)
        for child in self.child:
            child.depth_first_search_adj_list(res)
        return res 
    

graph = Node('A')
graph.add_child('B').add_child('C').add_child('D')
graph.child[0].add_child('E').add_child('F')
graph.child[2].add_child('G').add_child('H')
graph.child[0].child[1].add_child('I').add_child('J')
graph.child[2].child[0].add_child('K')
actual = ['A', 'B', 'E', 'F', 'I', 'J', 'C', 'D', 'G', 'K', 'H']
expected = graph.depth_first_search_adj_list([])
simple_assert(actual, expected)
