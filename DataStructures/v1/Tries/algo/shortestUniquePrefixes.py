def simple_assert(a, b):
    assert a == b, f"{a}!={b}"
    

def shortestUniquePrefixes(strings):
    trie = Trie()
    for string in strings:
        trie.insert(string)
    
    prefixes = []
    for string in strings:
        uniquePrefixes = findUniquePrefixes(string, trie)
        prefixes.append(uniquePrefixes)
    return prefixes

def findUniquePrefixes(string, trie):
    currentStrIdx = 0 
    currNode = trie.root 
    
    while currentStrIdx < len(string) - 1:
        currChar = string[currentStrIdx]
        currNode = currNode[currChar]
        if currNode["count"] == 1:
            break 
        currentStrIdx += 1
    return string[0:currentStrIdx + 1]

class Trie:
    def __init__(self):
        self.root = {"count" : 0}
    
    def insert(self, string):
        currNode = self.root
        for i in range(len(string)):
            letter = string[i]
            if letter not in currNode:
                currNode[letter] = {"count": 0}
            currNode = currNode[letter]
            currNode['count'] += 1
    




strings = ["algoexpert", "algorithm", "frontendexpert", "mlexpert"]
expected = ["algoe", "algor", "f", "m"]
actual = shortestUniquePrefixes(strings)
simple_assert(actual, expected)