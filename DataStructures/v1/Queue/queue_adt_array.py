class Queue:
    def __init__(self, n):
        self.front = -1
        self.rear = -1
        self.size = n
        self.Q = self.buildQueue()
    
    def buildQueue(self):
        self.Q = [0 for _ in range(self.size)]
        return self.Q 

    def Enqueue(self, value):
        if self.rear == self.size-1:
            raise"Overflow"
        else:
            self.rear +=1
            self.Q[self.rear] = value 
         
    def Dequeue(self):
        x = -1
        if self.rear == self.front:
            raise "Underflow"
        else:
            self.front += 1
            x = self.Q[self.front]
        return x

    def is_Empty(self):
        return len(self.Q)  == 0

    def is_Full(self):
        return self.rear == self.size-1  

    def peek(self):
        self.front += 1
        return self.Q[self.front]

    def peek_rear(self):
        return self.Q[self.rear] 

    def display(self):
        value = []
        for values in range(self.front+1, self.rear+1):
            value.append(self.Q[values])
        return value