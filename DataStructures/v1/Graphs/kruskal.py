def kruskalMST(edges, n, e):
    u,v,idx, k = 0, 0, 0, 0
    minVal = float("inf")
    visited = [0] * e 
    v = n - 1
    Kt = [[0] * v for _ in range(2)]
    
    while idx < n-1:
        minVal = float("inf")
        for j in range(e):
            if visited[j] == 0 and edges[2][j] < minVal:
                minVal = edges[2][j]
                u = edges[0][j]
                v = edges[1][j]
                k = j
        if find(u) != find(v):
            Kt[0][idx] = u
            Kt[1][idx] = v
            union(find(u),find(v))
            idx += 1
        visited[k] = 1
    
    for idx in range(n-1):
        print(f"( {Kt[0][idx]} , {Kt[1][idx]})")

def union(u, v):
    if unionSet[u] < unionSet[v]:
        unionSet[u] += unionSet[v]
        unionSet[v] = u
    else:
        unionSet[v] += unionSet[u]
        unionSet[u] = v 

def find(u):
    x, v = u, 0
    while unionSet[x] > 0:
        x = unionSet[x]
    while u != x:
        v = unionSet[u]
        unionSet[u] = x 
        u = v 
    return x 



    




if __name__=="__main__":
    edges = [[1, 1, 2, 2, 3, 4, 4, 5, 5],    
             [2, 6, 3, 7, 4, 5, 7, 6, 7], 
             [25, 5, 12, 10, 8, 16, 14, 20, 18]]
    edge, n = 9, 7
    unionSet = [-1] * edge 
    kruskalMST(edges, n, edge)
