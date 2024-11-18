def simple_assert(a, b):
    assert a == b, f"{a}!={b}"

class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        for i in range(len(string)):
            self.insertSubstringStartingAt(i, string)
    
    def insertSubstringStartingAt(self, startAt, string):
        node = self.root 
        for j in range(startAt, len(string)):
            letter = string[j]
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node[self.endSymbol] = True 
            

    def contains(self, string):
        # Write your code here.
        node = self.root
        for char in string:
            if char not in node:
                return False 
            node = node[char]
        return self.endSymbol in node 

trie = SuffixTrie("babc")
expected = {
    "c": {"*": True},
    "b": {"c": {"*": True}, "a": {"b": {"c": {"*": True}}}},
    "a": {"b": {"c": {"*": True}}},
}
simple_assert(trie.root, expected)
simple_assert(trie.contains("abc"), True)