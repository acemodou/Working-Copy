def simple_assert(a, b):
    assert a == b, f'{a}!{b}'

# O(v^2) time | O(v) space 
def bread_first_search_adj_matrix(matrix):
    res = bfs(matrix, 1)
    return res 

def bfs(matrix, start_idx):
    num_columns = len(matrix[0])
    
    visited = [0] * num_columns
    
    visited[start_idx] = 1
    queue = [start_idx]
    res =   [start_idx]
    
    while len(queue) > 0:
        u = queue.pop(0)
        
        for v in range(1, num_columns):
            if matrix[u][v] == 1 and visited[v] == 0:
                visited[v] = 1
                res.append(v)
                queue.append(v)
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
expected = bread_first_search_adj_matrix(adjacency_matrix)
simple_assert(actual, expected)

# O(V + E) time | O(V + E) space 
class Node:
    def __init__(self, name) -> None:
        self.name = name 
        self.child = [] 
    
    def add_child(self, name) -> None:
        self.child.append(Node(name))
        return self 

    def bread_first_search_adj_list(self, array):
        queue = [self]
        
        while len(queue) > 0:
            u = queue.pop(0)
            array.append(u.name)
            for child in u.child:
                queue.append(child)
        
        return array 
                

graph = Node('A')
graph.add_child('B').add_child('C').add_child('D')
graph.child[0].add_child('E').add_child('F')
graph.child[2].add_child('G').add_child('H')
graph.child[0].child[1].add_child('I').add_child('J')
graph.child[2].child[0].add_child('K')
actual = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
expected = graph.bread_first_search_adj_list([])
simple_assert(actual, expected)
