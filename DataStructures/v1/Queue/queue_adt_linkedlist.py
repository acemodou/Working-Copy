class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None 

class QueueLIST:
    def __init__(self):
        self.front = None 
        self.rear  = None 

    def Enqueue(self, value):
        node = Node(value)
        node.next = None 
        if self.isFull():
            raise"Overflow"
        else:
            if not self.front:
                self.front = node 
                self.rear  = node
                return 
            self.rear.next = node 
            self.rear = node 

    def Dequeue(self):
        x = -1
        if self.isEmpty():
            raise "Underflow"
        else:
            x = self.front.value 
            self.front = self.front.next 
        return x

    def isEmpty(self):
        return self.front == self.rear 

    def isFull(self):
        node = Node(0)
        node.next = None 
        return True if not node else False  

    def peek(self):
        return self.front.value 

    def peek_rear(self):
        return self.rear.value

    def display(self):
        value = []
        curr_ptr = self.front 
        while curr_ptr:
            value.append(curr_ptr.value)
            curr_ptr = curr_ptr.next 
        return value