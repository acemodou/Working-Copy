def simpleAssert(a, b):
    assert a == b, f'{a}!{b}'

# class MinMaxStack:
#     def __init__(self) -> None:
#         self.stack = []
#         self.minMax = []

#     def peek(self):
#         return self.stack[-1]

#     def pop(self):
#         poppedValue = self.peek()
#         self.minMax.pop()
#         self.stack.pop()
#         return poppedValue

#     def push(self, number):
#         newMinMax = {"min" : number, "max" : number}
#         if len(self.minMax):
#             lastMinMax = self.minMax[-1]
#             newMinMax["min"] = min(lastMinMax["min"], number)
#             newMinMax["max"] = max(lastMinMax["max"], number) 

#         self.minMax.append(newMinMax)
#         self.stack.append(number)
        
#     def getMin(self):
#         return self.minMax[-1]["min"]

#     def getMax(self):
#         return self.minMax[-1]["max"]

class Node:
    def __init__(self, v:int) -> None:
        self.value = v 
        self.next = None 
        
class MinMaxStack:
    def __init__(self) -> None:
        self.head = None 
        self.minMax = None
    
    def addLast(self, value : Node, isMinMaxNode=False) -> None:
        newNode = Node(value)
        newNode.next = self.minMax if isMinMaxNode else self.head
        if isMinMaxNode:
            self.minMax = newNode
        else:   
            self.head = newNode
    
    def removeLast(self, isLast : bool=False):
        popped = self.minMax if isLast else self.head
        if isLast:
            self.minMax = self.minMax.next
        else:
            self.head = self.head.next 
        popped.next = None
        popped = None 

    def peek(self):
        return self.head.value
    
    def pop(self):
        poppedValue= self.peek()
        self.removeLast(isLast=True)
        self.removeLast(isLast=False)
        return poppedValue

    def push(self, number : Node) -> None:
        newMinMax = {"min" : number, "max" : number}
        if self.minMax:
            lastMinMax = self.minMax.value
            newMinMax["min"] = min(lastMinMax["min"], number)
            newMinMax["max"] = max(lastMinMax["max"], number) 
        
        self.addLast(newMinMax, isMinMaxNode=True)
        self.addLast(number)

    def getMin(self):
        return self.minMax.value["min"]

    def getMax(self):
        return self.minMax.value["max"]

st = MinMaxStack()
simpleAssert(st.push(5), None)
simpleAssert(st.getMin(), 5)
simpleAssert(st.getMax(), 5)
simpleAssert(st.peek(), 5)
simpleAssert(st.push(7), None)
simpleAssert(st.getMin(), 5)
simpleAssert(st.getMax(), 7)
simpleAssert(st.peek(), 7)
simpleAssert(st.push(2), None)
simpleAssert(st.getMin(), 2)
simpleAssert(st.getMax(), 7)
simpleAssert(st.peek(), 2)
simpleAssert(st.pop(), 2)
simpleAssert(st.pop(), 7)
simpleAssert(st.getMax(), 5)
simpleAssert(st.getMin(), 5)
simpleAssert(st.peek(), 5)