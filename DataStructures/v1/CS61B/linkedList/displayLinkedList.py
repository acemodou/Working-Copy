""" Display the content in a linked list using both iterative and recursive """
class IntList:
    def __init__(self, f, r) -> None:
        self.first = f
        self.ref = r 
    
    def iterativeDisplay(self) -> None:
        ptr = self 
        while ptr:
            print(ptr.first)
            ptr = ptr.ref 
    
    def recursiveDisplay(self) -> None:
        self.recursiveDisplayHelper(self)
    
    def recursiveDisplayHelper(self, ptr):
        if ptr:
            print(ptr.first)
            self.recursiveDisplayHelper(ptr.ref)
    
    def Size(self):
        ptr = self 
        totalElements = 0
        while ptr:
            totalElements += 1
            ptr = ptr.ref 
        return totalElements

    def get(self, i):
        if i == 0:
            return self.first
        return self.ref.get(i-1)

    """We take a list and increment it by x"""


def incrList(L, x):
    if L is None:
        return None

    newList = IntList(L.first + x)
    oldList = L.ref 
    newTail = newList 

    while oldList:
        newTail.ref = IntList(oldList.first + x)
        oldList = oldList.ref 
        newTail = newTail.ref 
    return newList 

def dincrList(L, x):
    ptr = L 
    while ptr:
        ptr.first += x 
        ptr = ptr.ref 
    return L 

L = IntList(10, None)
L = IntList(5, L)
L = IntList(15, L)

# L.iterativeDisplay()
# L.recursiveDisplay()
# print(L.Size())
# print(L.get(2))
incrList(L, 2)
