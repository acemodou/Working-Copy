def simple_assert(a, b):
    assert a == b, f"{a}!{b}"

class Node:
    def __init__(self, name) -> None:
        self.name = name 
        self.children = []
    
    def addChildren(self, name):
        self.children.append(Node(name))
        return self 
    
    def breadthFirstSearch(self, array):
        queue = [self]
        
        while len(queue) > 0:
            current = queue.pop(0)
            array.append(current.name)
            for child in current.children:
                queue.append(child)
        return array 
         
    

graph = Node("A")
graph.addChildren("B").addChildren("C").addChildren("D")
graph.children[0].addChildren("E").addChildren("F")
graph.children[2].addChildren("G").addChildren("H")
graph.children[0].children[1].addChildren("I").addChildren("J")
graph.children[2].children[1].addChildren("K")
simple_assert(graph.breadthFirstSearch([]), ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"])