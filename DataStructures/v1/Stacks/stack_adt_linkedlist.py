
class Node:
    def __init__(self):
        self.value = None  
        self.next = None 

class STACKLIST:
    def __init__(self):
        self.top = None 

    def push(self, value):
        node = Node()
        node.value = value 
        if node is None:
            raise "Stack overflow"
        else:
            node.next = self.top 
            self.top = node 
    
    def pop(self):
        if not self.top:
            raise "Stack underflow"
        else:
            x = self.top.value
            curr_ptr = self.top
            self.top = self.top.next 
            curr_ptr.next = None 
            curr_ptr = None 
            return x 

    def peek(self, index):
        if not self.top:
            raise "Stack is empty" 
        ptr = self.top 
        for _ in range(index-1):
            ptr = ptr.next 
        return ptr.value if ptr else None 

    def isEmpty(self):
        return self.top is None 

    def isFull(self):
        dummy_value = 0
        node = Node()
        node.value = dummy_value
        return True if node else False 

    def stackTop(self):
        return self.top.value 
    
    def display(self):
        node = self.top
        values = [] 
        while node:
            values.append(node.value)
            node = node.next 
        return values
            