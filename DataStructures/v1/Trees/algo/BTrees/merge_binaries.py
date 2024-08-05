def simple_assert(a, b):
    assert a == b, f"{a}!{b}"

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(n) time and O(h) space
# def mergeBinaryTrees(tree1, tree2):
#     # Write your code here.
#     if tree1 is None:
#         return tree2
#     if tree2 is None:
#         return tree1

#     tree1.value += tree2.value 
#     tree1.left = mergeBinaryTrees(tree1.left, tree2.left)
#     tree1.right = mergeBinaryTrees(tree1.right, tree2.right)
#     return tree1 
    
def mergeBinaryTrees(tree1, tree2):
   if tree1 is None:
       return tree2
   
   tree1Stack = [tree1]
   tree2Stack = [tree2]

   while len(tree1Stack) > 0:
       tree1Node = tree1Stack.pop()
       tree2Node = tree2Stack.pop()

       if tree2Node is None:
           continue
       
       tree1Node.value += tree2Node.value 

       if tree1Node.left is None:
           tree1Node.left = tree2Node.left 
       else:
           tree1Stack.append(tree1Node.left)
           tree2Stack.append(tree2Node.left)
      
       if tree1Node.right is None:
           tree1Node.right = tree2Node.right 
       else:
           tree1Stack.append(tree1Node.right)
           tree2Stack.append(tree2Node.right)
   return tree1
       

tree1  =BinaryTree(1)
tree1.left = BinaryTree(3)
tree1.left.left = BinaryTree(7)
tree1.left.right = BinaryTree(4)
tree1.right = BinaryTree(2)

tree2 = BinaryTree(1)
tree2.left = BinaryTree(5)
tree2.left.left = BinaryTree(2)
tree2.right = BinaryTree(9)
tree2.right.left = BinaryTree(7)
tree2.right.right = BinaryTree(6)

actual = mergeBinaryTrees(tree1, tree2)
simple_assert(actual.value, 2)
simple_assert(actual.left.value, 8)
simple_assert(actual.left.left.value, 9)
simple_assert(actual.left.right.value, 4)
simple_assert(actual.right.value, 11)
simple_assert(actual.right.left.value, 7)
simple_assert(actual.right.right.value, 6)
