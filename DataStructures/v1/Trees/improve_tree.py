class Node:
    def __init__(self, data) -> None:
        self.left = None 
        self.right = None
        self.data = data 

# lEAF_NODE = -1

# class BinaryTree:
#     def __init__(self) -> None:
#         self.root = None 

#     def create_root(self, value):
#         self.root = Node(value)

#     # def insert(self, root, values):
#     #     Q = []
#     #     temp = None
#     #     pointer = None
#     #     Q.append(root)
#     #     idx = 1

#     #     while Q and idx < len(values):
#     #         pointer = Q.pop(0)
#     #         left_value = values[idx]
#     #         idx += 1
#     #         if left_value != lEAF_NODE:
#     #             temp = Node(left_value)
#     #             pointer.left = temp
#     #             Q.append(pointer.left)
#     #         idx +=1
#     #         right_value = values[idx]
#     #         if right_value != lEAF_NODE:
#     #             temp = Node(right_value)
#     #             pointer.right = temp
#     #             Q.append(pointer.right)
     
def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root 
 
def preorder(root):
    if root:
        print(root.data)
        preorder(root.left)
        preorder(root.right)
    
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

def postoder(root):
    if root:
        postoder(root.left)
        postoder(root.right)
        print(root.data)
    
def levelorder(root):
    queue = []
    print(root.data)
    queue.append(root)
    while queue:
        ptr = queue.pop(0)
        if ptr.left:
            print(ptr.left.data)
            queue.append(ptr.left)
        if ptr.right:
            print(ptr.right.data)
            queue.append(ptr.right)
            

# # Driver code
# values = [50, 30, 70, 20, 40, 60, 80, 10, -1, -1, -1, -1, -1, -1, -1, -1, -1]
# T = BinaryTree()
# T.create_root(values[0])
# T.insert(T.root, values[1:])
# T.pre_order(T.root)
# print("In order traversal: ..............................")
# T.in_order(T.root)

# Driver code
root = None 
root = insert(root, 50)
insert(root, 30)
insert(root, 70)
insert(root, 20)
insert(root, 40)
insert(root, 60)
insert(root, 80)
insert(root, 10)
preorder(root)
print("In order traversal of the binary tree is: ")
inorder(root)
print("Postorder traversal of the binary tree is: ")
postoder(root)
print("Level order traversal :")
levelorder(root)