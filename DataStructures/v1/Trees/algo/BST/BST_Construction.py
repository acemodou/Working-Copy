def simple_assert(a, b):
    assert a == b, f'{a}!{b}'

class BST:
    def __init__(self, value : int) -> None:
        self.value = value 
        self.left = None 
        self.right = None 
    
    def insert(self, value : int) -> int:
        currentNode = self 
        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left 
            else:
                if currentNode.right is None:
                    currentNode.righ = BST(value)
                    break 
                else:
                    currentNode = currentNode.right
        return self 
    
    def contains(self, value : int) -> int:
        currentNode = self 
        while currentNode is not None:
            if value == currentNode.value:
                return True 
            elif value < currentNode.value:
                currentNode = currentNode.left 
            else:
                currentNode = currentNode.right 
        return False 

    # def remove(self, value):
    #     if self is None:
    #         return None

    #     if self.value == value:
    #         # Handle the case when the node to be removed is the root
    #         if self.left is None:
    #             temp = self.right
    #             self = None
    #             return temp
    #         elif self.right is None:
    #             temp = self.left
    #             self = None
    #             return temp

    #         if self.height(self.left) > self.height(self.right):
    #             q = self.inorder_predecessor(self.left)
    #             self.value = q.value
    #             self.left = self.left.remove(q.value)
    #         else:
    #             q = self.inorder_successor(self.right)
    #             self.value = q.value
    #             self.right = self.right.remove(q.value)
    #         return self

    #     if value < self.value:
    #         self.left = self.left.remove(value)
    #     else:
    #         self.right = self.right.remove(value)
    #     return self
    def remove(self, value, parent=None):
        if value < self.value:
            if self.left is not None:
                self.left.remove(value, self)
        elif value > self.value:
            if self.right is not None:
                self.right.remove(value, self)
        else:
            if self.left is not None and self.right is not None:
                self.value = self.right.getMinValue()
                self.right.remove(self.value, self)
            elif parent is None:
                if self.left is not None:
                    self.value = self.left.value
                    self.right = self.left.right
                    self.left = self.left.left
                elif self.right is not None:
                    self.value = self.right.value
                    self.left = self.right.left
                    self.right = self.right.right
                else:
                    # this is a single-node tree; do nothing 
                    pass 
            elif parent.left == self:
                parent.left = self.left if self.left is not None else self.right
            elif parent.right == self:
                parent.right = self.left if self.left is not None else self.right
        return self 
    
   
bst = BST(10)
bst.left = BST(5)
bst.right = BST(15)
bst.left.left = BST(2)
bst.left.right = BST(5)
bst.right.left = BST(13)
bst.right.right = BST(22)
bst.left.left.left = BST(1)
bst.right.left.right = BST(14)

bst.insert(12)
simple_assert(bst.contains(10), True)
