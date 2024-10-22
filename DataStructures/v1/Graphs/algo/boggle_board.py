def simple_assert(a, b):
    assert a == b, f'{a}!{b}'

def boggleBoard(board, words):
    trie = Trie()
    for word in words:
        trie.add(word)
    finalWords = {}
    visited = [[False for _ in row] for row in board]
    for i in range(len(board)):
        for j in range(len(board[i])):
            explore(board, i, j, visited, finalWords, trie.root)
    return list(finalWords.keys())

def explore(board, i, j, visited, finalWords, trieNode):
    if visited[i][j]:
        return 
    
    letter = board[i][j]  
    if letter not in trieNode:
        return 
    visited[i][j] = True 
    trieNode = trieNode[letter]
    if "*" in trieNode:
        finalWords[trieNode["*"]] = True 
    
    neighbors = getNeighbors(board, i, j)
    for neighbor in neighbors:
        explore(board, neighbor[0], neighbor[1], visited, finalWords, trieNode)
    visited[i][j] = False 

def getNeighbors(board, i, j):
    numRows = len(board) - 1
    numCols = len(board[0]) - 1 
    neighbors = []
    
    if i > 0 and j > 0:
        neighbors.append([i - 1, j - 1])
    if i > 0 and j < numCols:
        neighbors.append([i - 1, j + 1])
    if i < numRows and j < numCols:
        neighbors.append([i + 1, j + 1])
    if i < numRows and j > 0:
        neighbors.append([i + 1, j - 1])
    if i > 0:
        neighbors.append([i-1, j])
    if i < numRows:
        neighbors.append([i + 1, j])
    if j > 0:
        neighbors.append([i, j-1])
    if j < numCols:
        neighbors.append([i, j + 1])
    return neighbors
        
class Trie:
    def __init__(self) -> None:
        self.root = {}
        self.endSymbol = '*'
    
    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.endSymbol] = word
            

board = [
        ["t", "h", "i", "s", "i", "s", "a"],
        ["s", "i", "m", "p", "l", "e", "x"],
        ["b", "x", "x", "x", "x", "e", "b"],
        ["x", "o", "g", "g", "l", "x", "o"],
        ["x", "x", "x", "D", "T", "r", "a"],
        ["R", "E", "P", "E", "A", "d", "x"],
        ["x", "x", "x", "x", "x", "x", "x"],
        ["N", "O", "T", "R", "E", "-", "P"],
        ["x", "x", "D", "E", "T", "A", "E"],
    ]

words = [
    "this",
    "is",
    "not",
    "a",
    "simple",
    "boggle",
    "board",
    "test",
    "REPEATED",
    "NOTRE-PEATED",
]

expected = ["this", "is", "a", "simple", "boggle", "board", "NOTRE-PEATED"]
actual = boggleBoard(board, words)
simple_assert(len(actual), len(expected))
for word in actual:
    simple_assert(word in expected, True)