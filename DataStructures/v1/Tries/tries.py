class Tries:
    def __init__(self):
        self.root = {"*":"*"}

    def add_word(self, words):
        curr_word = self.root 
        for word in words:
            if word not in curr_word:
                curr_word[word] = {}
            curr_word = curr_word[word]
        curr_word["*"] = "*"

    def does_word_exist(self, words):
        curr_word = self.root 
        for word in words:
            if word not in curr_word:
                return False 
            curr_word = curr_word[word]
        return "*" in curr_word

class TrieNode:
    def __init__(self, word):
        self.letter = word 
        self.children = {}
        self.is_end_of_word = False 

class NodeTries:
    def __init__(self):
        self.root = TrieNode("*")
    
    def add_word(self, words):
        curr_node = self.root 
        for word in words:
            if word not in curr_node.children:
                curr_node.children[word] = TrieNode(word)
            curr_node = curr_node.children[word]
        curr_node.is_end_of_word = True 
    
    def does_word_exist(self, words):
        if words == "":
            return True
        curr_node = self.root
        for word in words:
            if word not in curr_node.children:
                return False 
            curr_node = curr_node.children[word]
        return curr_node.is_end_of_word 
