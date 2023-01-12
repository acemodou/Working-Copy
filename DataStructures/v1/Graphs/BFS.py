from collections import defaultdict

class Graph:
    def __init__(self):
        # add the graphs in a dictionary using defaultdict
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def BFS(self, s):
        visited = [False] * (max(self.graph) + 1)
        outputResult = []

        queue = []
        queue.append(s)
        visited[s] = True 

        while queue:
            s = queue.pop(0)
            outputResult.append(s)
            for edges in self.graph[s]:
                if visited[edges] == False:
                    queue.append(edges)
                    visited[edges] = True 
        
        return outputResult
