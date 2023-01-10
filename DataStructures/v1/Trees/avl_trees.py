class Node:
    def __init__(self, value):
        self.left = None 
        self.value = value 
        self.right = None 

class AvlTrees:
    def __init__(self) -> None:
        self.root = None 
        self.bf = 0 
        self.temp = self.root 
          
    def insert(self,node, key):
        if node is None: 
            temp = Node(key)
            temp.left, temp.right = None, None
            temp.bf = 0
            return temp
        if key < node.value:
            node.left = self.insert(node.left,key)
        else:
            node.right = self.insert(node.right, key) 
        lbf = self.height(node.left)
        rbf = self.height(node.right) 
        node.bf = lbf - rbf 
        if node.bf == 2 and node.left.bf == 1:
            self.llrotation(node)
        elif node.bf == 2 and node.left.bf == -1:
            self.lrRotation(node)
        elif node.bf == 2 and node.left.bf == -1:
            self.rrRotation(node)
        elif node.bf == 2 and node.left.bf == -1:
            self.rlrRotation(node)
        
        return node 
    
    def llrotation(self, node):
        pl = node.left
        plr = pl.right 
        pl.right = node 
        node.left = plr  
       
        lbf = self.height(node.left) + 1
        rbf = self.height(node.right) + 1
        node.bf = lbf - rbf 
        if node == self.root:
            self.root = pl 
        return pl 

    def lrRotation(self, node):
        pl = node.left 
        plr = pl.right
        plr.bf = 0
        node.left = plr.right
        pl.right = plr.left
        
        plr.left = pl 
        plr.right = node
        lbf = self.height(node.left) + 1
        rbf = self.height(node.right) + 1
        node.bf = lbf - rbf

        lbf = self.height(pl.left) + 1
        rbf = self.height(pl.right) + 1
        pl.bf = lbf - rbf  
        if node == self.root:
            self.root = plr 
        return plr 

    def rrRotation(self, node):
        pass 
    def rlRotation(self, node):
        pass 

    def height(self, node):
        if not node:
            return 0 
        x = self.height(node.left)
        y = self.height(node.right)
        return x + 1 if x > y else y + 1
    
program = AvlTrees()
program.root = program.insert(program.root, 50)
program.insert(program.root, 10)
program.insert(program.root, 20)
