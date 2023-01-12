class CircularQueue:
    def __init__(self, n):
        self.front = 0
        self.rear = 0
        self.size = n
        self.Q = self.buildQueue()
    
    def buildQueue(self):
        self.Q = [0 for _ in range(self.size)]
        return self.Q 

    def Enqueue(self, value):
        if self.is_Full():
            raise"Overflow"
        else:
            self.rear = self.rear +1 % self.size
            self.Q[self.rear] = value 
         
    def Dequeue(self):
        x = -1
        if self.is_Empty():
            raise "Underflow"
        else:
            self.front = self.front +1 % self.size
            x = self.Q[self.front]
        return x

    def is_Empty(self):
        return self.rear == self.front 

    def is_Full(self):
        return self.rear +1 % self.size == self.front 

    def peek(self):
        self.front += 1
        return self.Q[self.front]

    def peek_rear(self):
        return self.Q[self.rear] 

    def display(self):
        value = []
        for values in range(self.front+1, self.rear +1 % self.size):
            value.append(self.Q[values])
        return value