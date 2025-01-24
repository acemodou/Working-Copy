def simple_assert(a, b):
    assert a == b, f'{a}!{b}'  
    
# O(n!) time | O(n!) space 
def string_permutation(strs):
    leafs = [0] * len(strs)
    visited = [0] * len(strs)
    res = backtrack(strs, 0, [], leafs, visited)
    joined_res = ["".join(leaves) for leaves in res]
    return joined_res

def backtrack(strs, k, res, leafs, visited):
    if len(strs) == k:
        res.append(leafs[:])
    
    for i in range(len(strs)):
        if visited[i] == 0:
            leafs[k] = strs[i]
            visited[i] = 1
            backtrack(strs, k+1, res, leafs, visited)
            visited[i] = 0
    return res 
  

expected = ["ABC", "ACB", "BAC", "BCA", "CAB", "CBA"]
actual = string_permutation("ABC")
simple_assert(expected, actual)

 