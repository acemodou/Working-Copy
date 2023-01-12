class STACK:
    def __init__(self, n):
        self.size = n
        self.top = -1
        self.stack = []
    
    def initialize(self):
        self.stack = [0] * self.size  

    def Display(self):
        for items in reversed(range(self.top)):
            self.stack[items]
        return self.stack

    def Push(self, value):
        # if the stack is full we shouldn't add and element to it
        # otherwise at and element to the stack
        if self.top == self.size-1:
            raise("Overflow !!!!")
        else:
            self.top +=1 
            self.stack[self.top] = value

    def Pop(self):
        if self.top == -1:
            raise("Underflow !!!")
        else:
            deleted_value = self.stack[self.top]
            self.top -= 1
        return deleted_value 

    def Peek(self, idx):
        if self.top < 0:
            raise("Overflow")
        else:
            value = self.stack[(self.top-idx)+1]
        return value 

    def isEmpty(self):
        return self.top == -1
        
    def isFull(self):
        return self.top == self.size-1 

    def stackTop(self):
        if self.isEmpty():
            raise("Stack is empty")
        return self.stack[self.top]

