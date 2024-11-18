def simple_assert(a, b):
    assert a == b, f"{a}!={b}"
    
    
def longestMostFrequentPrefix(strings):
    trie = Trie()
    for string in strings:
        trie.insert(string)
    return trie.maxPrefixFullString[0: trie.maxPrefixLength]

class Trie:
    def __init__(self):
        self.root = {"count" : 0}
        self.maxPrefixCount = 0 
        self.maxPrefixLength = 0 
        self.maxPrefixFullString = ""
    
    def insert(self, string):
        currNode = self.root
        for i in range(len(string)):
            letter = string[i]
            if letter not in currNode:
                currNode[letter] = {"count": 0}
            currNode = currNode[letter]
            currNode['count'] += 1
            
            if currNode['count'] > self.maxPrefixCount:
                self.maxPrefixCount = currNode['count']
                self.maxPrefixLength = i + 1
                self.maxPrefixFullString = string
            elif currNode['count'] == self.maxPrefixCount and i + 1 > self.maxPrefixLength:
                self.maxPrefixLength = i + 1
                self.maxPrefixFullString = string 

strings = [
        "algoexpert",
        "algorithm",
        "frontendexpert",
        "mlexpert",
    ]
expected = "algo"
actual = longestMostFrequentPrefix(strings)
simple_assert(actual, expected)
