def simple_assert(a, b):
    assert a == b, f'{a}!{b}'


def twoColorable(edges):
    # Write your code here.
    colors = [None] * len(edges)
    colors[0] = True 
    stack = [0]
    
    while len(stack) > 0:
        node = stack.pop(0)
        
        for connection in edges[node]:
            if colors[connection] is None:
                colors[connection] = not colors[node]
                stack.append(connection)
            elif colors[connection] == colors[node]:
                return False 
    return True 



input = [[1], [0]]
expected = True
actual = twoColorable(input)
simple_assert(actual, expected)