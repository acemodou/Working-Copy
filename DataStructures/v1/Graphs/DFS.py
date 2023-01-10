
from collections import defaultdict
class Graph:
    def __init__(self):
        # add the graphs in a dictionary using defaultdict
        self.graph = defaultdict(list)
        self.visited = set()
        self.result = []
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def DFS(self, value):
        if value not in self.visited:
            self.result.append(value)
            self.visited.add(value)
            for neighbours in self.graph[value]:
                self.DFS(neighbours)
        return self.result
