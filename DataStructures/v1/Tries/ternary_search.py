class Node:
    def __init__(self, char):
        self.char = char 
        self.leftNode = None 
        self.rightNode = None 
        self.middleNode = None 

class TST:
    def __init__(self) -> None:
        self.rootNode = None 
    
    def put(self, key, value):
        self.rootNode = self.putItem(self.rootNode, key, value, 0)
    
    def putItem(self, node, key, value, index):
        strs_char = key[index]

        if node == None:
            node = Node(strs_char)
        if strs_char < node.char:
            node.leftNode = self.putItem(node.leftNode, key, value, index)
        elif strs_char > node.char:
            node.rightNode = self.putItem(node.rightNode, key, value, index)
        elif index < len(key)-1:
            node.middleNode = self.putItem(node.middleNode, key, value, index+1)
        else:
            node.value = value 
        return node
    
    def get(self, key):
        node = self.getItem(self.rootNode, key, 0)
        if node == None:
            return None 
        return node.value 
    
    def getItem(self, node, key, index):
        if node == None:
            return None 
        
        strs_char = key[index]
        
        if strs_char < node.char:
            return self.getItem(node.leftNode, key, index)
        elif strs_char > node.char:
            return self.getItem(node.rightNode, key, index)
        elif index < len(key)-1:
            return self.getItem(node.middleNode, key, index+1)
        else:
            return node
