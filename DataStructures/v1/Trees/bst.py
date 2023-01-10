
class Node:
    def __init__(self, value):
        self.lchild = None 
        self.value = value
        self.rchild = None 

class BST:
    def __init__(self):
        self.temp = None
        self.root = None 
    
    def insert(self, key):
        self.temp = self.root
        self.r = self.temp 
        # Root is empty 
        if self.root is None:
            self.root = Node(key)
            self.root.lchild = None 
            self.root.rchild = None 
            return 
        
        while self.temp:
            self.r = self.temp 
            if key < self.temp.value:
                self.temp = self.temp.lchild 
            elif key > self.temp.value:
                self.temp = self.temp.rchild
            else:
                return 
        # Now temp points at Null and r points at insert location
        self.temp = Node(key)
        self.temp.lchild = None 
        self.temp.rchild = None 

        if key < self.r.value:
            self.r.lchild = self.temp
        else:
            self.r.rchild = self.temp
    


    def in_order(self, node):
        if node:
            self.in_order(node.lchild)
            print(node.value)
            self.in_order(node.rchild) 
    
    def search(self, key):
        self.temp = self.root
        while self.temp:
            if key == self.temp.value:
                return self.temp.value 
            elif key < self.temp.value:
                self.temp = self.temp.lchild
            else:
                self.temp = self.temp.rchild
        return None
    
    def tree_height(self, root):
        if not root:
            return 0 
        x = self.tree_height(root.lchild)
        y = self.tree_height(root.rchild)
        return x + 1 if x > y else y + 1 
    
    def delete(self, root, key):

        if not root:
            return None

        #If it's a leaf node we delete as well  
        if not root.lchild and not root.rchild:
            if root == self.root:
                root.lchild = None 
                root.rchild = None 
                root = None 
                return None
            root = None
            return None   
        
        # Search for the key 
        if key < root.value:
            root.lchild = self.delete(root.lchild, key)
        elif key > root.value:
            root.rchild = self.delete(root.rchild, key)
        # Key is found, delete it from the longest height 
        else:
            if self.tree_height(root.lchild) > self.tree_height(root.rchild):
                q = self.inorder_predecessor(root.lchild)
                root.value = q.value 
                root.lchild = self.delete(root.lchild, q.value)
            else:
                q = self.inoder_successor(root.rchild)
                root.value = q.value
                root.lchild = self.delete(root.lchild, q.value)
        return root
    
    def inorder_predecessor(self, node):
        while node and node.rchild:
            node = node.rchild
        return node 
    
    def inoder_successor(self, node):
        while node and node.lchild:
            node = node.lchild
        return node 
    
  

bst = BST()
bst.insert(50)
bst.insert(10)
bst.insert(40)
bst.insert(20)
bst.insert(30)

bst.delete(bst.root, 30)
bst.in_order(bst.root)
# print(bst.search(2))
# bst.in_order(bst.root)
