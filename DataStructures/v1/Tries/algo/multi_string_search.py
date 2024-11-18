def simple_assert(a, b):
    assert a == b, f"{a}!={b}"


# def multiStringSearch(bigString, smallStrings):
#    return [isInBigString(bigString, smallString) for smallString in smallStrings]

# def isInBigString(bigString, smallString):
#     for i in range(len(bigString)):
#         if i + len(smallString) > len(bigString):
#             break 
#         if isInBigStringHelper(bigString, smallString, i):
#             return True 
#     return False 

# def isInBigStringHelper(bigString, smallString, startIdx):
#     leftBigIdx = startIdx
#     rightBigIdx = startIdx + len(smallString) - 1
#     leftSmallIdx = 0 
#     righSmallIdx = len(smallString) -1
    
#     while leftBigIdx <= rightBigIdx:
#         if (bigString[leftBigIdx] != smallString[leftSmallIdx]
#             or bigString[rightBigIdx] != smallString[righSmallIdx]):
#             return False 
#         leftBigIdx += 1
#         rightBigIdx -= 1
#         leftSmallIdx += 1
#         righSmallIdx -= 1
#     return True 
         

def multiStringSearch(bigString, smallStrings):
    trie = Trie()
    for string in smallStrings:
        trie.insert(string)
    
    containedStrings = {}
    for i in range(len(bigString)):
        findSmallStringIn(bigString, i, trie, containedStrings)
    
    return [string in containedStrings for string in smallStrings]
    

def findSmallStringIn(string, startIdx, trie, containedStrings):
    currentNode = trie.root 
    for i in range(startIdx, len(string)):
        currentChar = string[i]
        if currentChar not in currentNode:
            break 
        currentNode = currentNode[currentChar]
        if trie.endSymbol in currentNode:
            containedStrings[currentNode[trie.endSymbol]] = True 
        
    

class Trie:
    def __init__(self):
        self.root = {}
        self.endSymbol  = "*"
    
    def insert(self, string):
        node = self.root 
        for i in range(len(string)):
            letter = string[i]
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node[self.endSymbol] = string 

simple_assert(
multiStringSearch(
"this is a big string", ["this", "yo", "is", "a", "bigger", "string", "kappa"]),
[True, False, True, True, False, True, False],)