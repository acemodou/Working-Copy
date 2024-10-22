def simple_assert(a, b):
    assert a == b, f'{a}!{b}'

WHITE, GREY, BLACK = 0, 1, 2

def cycleInGraph(edges):
    numOfNodes = len(edges)
    
    colors = [WHITE for _ in range(numOfNodes)]
    
    for node in range(numOfNodes):
        if colors[node] != WHITE:
            continue 
        containCycle = traverseAndColorNodes(node, edges, colors)
        if containCycle:
            return True 
    return False 

def traverseAndColorNodes(node, edges, colors):
    colors[node] = GREY
    
    neighbors = edges[node]
    for neighbor in neighbors:
        neighborColor = colors[neighbor]
        
        if neighborColor == GREY:
            return True
         
        if neighborColor == BLACK:
            continue
        
        containCycle = traverseAndColorNodes(neighbor, edges, colors)
        if containCycle:
            return True 
    colors[node] = BLACK
    return False 
        

input = [[1, 3], [2, 3, 4], [0], [], [2, 5], []]
expected = True
actual = cycleInGraph(input)
simple_assert(actual, expected)