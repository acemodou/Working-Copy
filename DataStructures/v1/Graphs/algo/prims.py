def printMST(T, G):
    print("\nMinimum Spanning Tree Edges (w/ cost)\n")
    sum = 0
    for i in range(6):
        c = G[T[0][i]][T[1][i]]
        print(f"[ << {T[0][i]} << ]---[ << {T[1][i]} << ] cost:{c}")
        sum += c
    print(f"\n Total cost of MST: {sum}")
    
def primsMST(G):
    u, v = 0,0 
    V = 8
    min = float("inf")
    track = [float("inf")] * V
    T= [[0] * 7 for _ in range(2)]
    for i in range(1, len(G)):
        track[i] = float("inf")
        for j in range(i,V):
            if G[i][j] < min:
                min = G[i][j]
                u, v = i, j
    T[0][0] = u
    T[1][0] = v
    
    track[u], track[v] = 0, 0
    
    for i in range(1, V):
        if track[i] != 0:
            if G[i][u] < G[i][v]:
                track[i] = u
            else:
                track[i] = v
    
    for i in range(1, len(G)-1):
        k = 0
        min = float("inf")
        for j in range(1, V):
            if track[j] != 0 and G[j][track[j]] < min:
                k = j
                min = G[j][track[j]]
        T[0][i] = k
        T[1][i] = track[k]
        track[k] = 0
        
        # Update track array to track min cost edges
        for j in range(1, V):
            if track[j] != 0 and G[j][k] < G[j][track[j]]:
                track[j] = k
    printMST(T, G)
   

if __name__ =="__main__":
    cost = [
                [float("inf"), float("inf"), float("inf"), float("inf"), float("inf"), float("inf"), float("inf"), float("inf")],
                [float("inf"), float("inf"), 25, float("inf"), float("inf"), float("inf"), 5, float("inf")],
                [float("inf"), 25, float("inf"), 12, float("inf"), float("inf"), float("inf"), 10],
                [float("inf"), float("inf"), 12, float("inf"), 8, float("inf"), float("inf"), float("inf")],
                [float("inf"), float("inf"), float("inf"), 8, float("inf"), 16, float("inf"), 14],
                [float("inf"), float("inf"), float("inf"), float("inf"), 16, float("inf"), 20, 18],
                [float("inf"), 5, float("inf"), float("inf"), float("inf"), 20, float("inf"), float("inf")],
                [float("inf"), float("inf"), 10, float("inf"), 14, 18, float("inf"), float("inf")]
            ]
primsMST(cost)
   