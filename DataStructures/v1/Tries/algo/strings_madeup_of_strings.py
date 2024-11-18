def simple_assert(a, b):
    assert a == b, f"{a}!={b}"


def stringsMadeUpOfStrings(strings, substrings):
    trie = Trie()
    for substring in substrings:
        trie.insert(substring)
    
    results = []
    for string in strings:
        if isMadeUpOfStrings(string, 0, trie, {}):
            results.append(string)
    return results

def isMadeUpOfStrings(string, startIdx, trie, memo):
    if startIdx == len(string):
        return True 
    if startIdx in memo:
        return memo[startIdx]
    
    currentNode = trie.root 
    for currIdx in range(startIdx, len(string)):
        currChar = string[currIdx]
        if currChar not in currentNode:
            break 
        currentNode = currentNode[currChar]
        if currentNode["isEndOfString"] and \
            isMadeUpOfStrings(string, currIdx    +1,  trie, memo):
            memo[startIdx] = True 
            return True 
    
    memo[startIdx] = False 
    return False 
    

class Trie:
    def __init__(self):
        self.root = {"isEndOfString" : False }
    
    def insert(self, string):
        currentNode = self.root 
        for i in range(len(string)):
            letter = string[i]
            if letter not in currentNode:
                currentNode[letter] = {"isEndOfString" : False }
            currentNode = currentNode[letter]
        currentNode["isEndOfString"] = True 


strings = ["bar", "are", "foo", "ba", "b", "barely"]
substrings = ["b", "a", "r", "ba", "ar", "bar"]
expected = ["bar", "ba", "b"]
actual = stringsMadeUpOfStrings(strings, substrings)
simple_assert(actual, expected)
