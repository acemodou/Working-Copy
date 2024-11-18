from heapq import heappush, heappop

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.weight = 0  # Initialize weight for each node

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, weight=0):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.weight = weight  # Assign weight to the end of the word node

    def search_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def _collect_words(self, node, prefix, heap):
        if node.is_end_of_word:
            heappush(heap, (-node.weight, prefix))  # Use negative weight for max-heap behavior
        for char, child_node in node.children.items():
            self._collect_words(child_node, prefix + char, heap)

    def autocomplete(self, prefix, limit=5):
        node = self.search_prefix(prefix)
        heap = []
        if node:
            self._collect_words(node, prefix, heap)
        
        # Retrieve up to `limit` items sorted by weight
        results = []
        while heap and len(results) < limit:
            weight, word = heappop(heap)
            results.append((word, -weight))  # Convert weight back to positive
        return results


# Example usage:
trie = Trie()
words_with_weights = [("cat", 20), ("car", 17), ("cart", 10), ("dog", 5), ("dove", 15), ("dot", 12)]
for word, weight in words_with_weights:
    trie.insert(word, weight)

# Autocomplete for prefix "ca" sorted by weight
print(trie.autocomplete("ca"))  # Output: [('cat', 20), ('car', 17), ('cart', 10)]
# Autocomplete for prefix "do" sorted by weight
print(trie.autocomplete("do"))  # Output: [('dove', 15), ('dot', 12), ('dog', 5)]
