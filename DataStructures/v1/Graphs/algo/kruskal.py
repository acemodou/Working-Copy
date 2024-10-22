import sys

# Constants
I = sys.maxsize  # Infinity
V = 7  # Number of vertices in the graph
E = 9  # Number of edges in the graph

# Function to print the Minimum Cost Spanning Tree
def print_mcst(T, A):
    print("\nMinimum Cost Spanning Tree Edges\n")
    for i in range(V - 1):
        print(f"[{T[0][i]}]-----[{T[1][i]}]")
    print()

# Union operation for the disjoint set
def union(u, v, s):
    if s[u] < s[v]:
        s[u] += s[v]
        s[v] = u
    else:
        s[v] += s[u]
        s[u] = v

# Find operation for the disjoint set
def find(u, s):
    x = u
    v = 0

    while s[x] > 0:
        x = s[x]

    while u != x:
        v = s[u]
        s[u] = x
        u = v

    return x

# Kruskal's Minimum Cost Spanning Tree Algorithm
def kruskals_mcst(A):
    T = [[0] * (V - 1) for _ in range(2)]  # Solution array
    track = [0] * E  # Track edges included in the solution
    set_ = [-1] * (V + 1)  # Array for finding cycle

    i = 0
    while i < V - 1:
        min_cost = I
        u, v, k = 0, 0, 0

        # Find a minimum cost edge
        for j in range(E):
            if track[j] == 0 and A[2][j] < min_cost:
                min_cost = A[2][j]
                u = A[0][j]
                v = A[1][j]
                k = j

        # Check if the selected min cost edge (u, v) forms a cycle or not
        if find(u, set_) != find(v, set_):
            T[0][i] = u
            T[1][i] = v

            # Perform union
            union(find(u, set_), find(v, set_), set_)
            i += 1

        track[k] = 1

    print_mcst(T, A)

if __name__ == "__main__":
    edges = [
        [1, 1, 2, 2, 3, 4, 4, 5, 5],
        [2, 6, 3, 7, 4, 5, 7, 6, 7],
        [25, 5, 12, 10, 8, 16, 14, 20, 18]
    ]

    kruskals_mcst(edges)
