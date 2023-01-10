
import queue_adt_linkedlist
from stack_adt_linkedlist import STACKLIST

class Node:
    def __init__(self, value):
        self.left_child = None 
        self.value = value
        self.right_child = None 

class Tree:
    def __init__(self):
        self.Q = queue_adt_linkedlist.QueueLIST()
        self.pointer = None 
        self.temp = None
        self.root = None 
        
    def create_tree(self):
        value = int(input("Enter root value: "))
        self.root = Node(value)
        self.root.left_child = None 
        self.root.right_child = None
        self.Q.Enqueue(self.root)

        while not self.Q.isEmpty():
            self.pointer = self.Q.Dequeue()
            data = int(input(f"Enter the left child of {self.pointer.value} :"))
            if data != -1:
                self.temp = Node(data)
                self.temp.left_child = None 
                self.temp.right_child = None 
                self.pointer.left_child = self.temp 
                self.Q.Enqueue(self.temp)
            data = int(input(f"Enter the right child of {self.pointer.value} :"))
            if data != -1:
                self.temp = Node(data)
                self.temp.left_child = None 
                self.temp.right_child = None 
                self.pointer.right_child = self.temp 
                self.Q.Enqueue(self.temp)
            
    def pre_order(self, node):
        if node:
            print(node.value)
            self.pre_order(node.left_child)
            self.pre_order(node.right_child)
    
    def IPre_order(self, node):
        st = STACKLIST()
        while node or not st.isEmpty():
            if node:
                print(node.value)
                st.push(node)
                node = node.left_child 
                
            else:
                ptr = st.pop()
                node = ptr.right_child 
                
    def post_order(self, node):
        if node:
            self.post_order(node.left_child)
            self.post_order(node.right_child)
            print(node.value)
    
    def Ipost_order(self, node):
        st = STACKLIST()
        while node or not st.isEmpty():
            if node:
                st.push(node)
                node = node.left_child  
            else:
                ptr = st.pop()
                if ptr.value > 0:
                    node = ptr 
                    ptr = ptr.value * -1
                    st.push(Node(ptr))
                    node = node.right_child
                else:
                    print(ptr.value *-1)
                    ptr = None 

    def in_order(self, node):
        if node:
            self.in_order(node.left_child)
            print(node.value)
            self.in_order(node.right_child)
    
    def IIn_order(self, node):
        st = STACKLIST()
        while node or not st.isEmpty():
            if node:
                st.push(node)
                node = node.left_child  
            else:
                ptr = st.pop()
                print(ptr.value)
                node = ptr.right_child 
         
    def level_order(self, node):
        print(node.value)
        self.Q.Enqueue(node)
        while not self.Q.isEmpty():
            ptr = self.Q.Dequeue()
            if ptr.left_child:
                print(ptr.left_child.value)
                self.Q.Enqueue(ptr.left_child)
            if ptr.right_child:
                print(ptr.right_child.value)
                self.Q.Enqueue(ptr.right_child)
    
    def count_nodes(self,root):
        if root:
            x = self.count_nodes(root.left_child)
            y = self.count_nodes(root.right_child)
            return x + y + 1 
        return 0
    
    def tree_height(self, root):
        if not root:
            return 0 
        x = self.tree_height(root.left_child)
        y = self.tree_height(root.right_child)
        return x + 1 if x > y else y + 1 

program = Tree()
program.create_tree()
# print(program.count_nodes(program.root))
print(program.tree_height(program.root))