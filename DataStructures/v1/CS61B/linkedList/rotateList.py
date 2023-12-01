from sentinel import SLList

class VengefulList(SLList):
    deletedItems = SLList()

    #Override removeLast 
    def removeLast(self):
        x =  super().removeLast()
        self.deletedItems.addLast(x)
        return x 
    
    def printLostItems(self):
        self.deletedItems.iterativeDisplay()
    

def rotateRight(head):
    x = head.removeLast()
    head.addFirst(x)




rs1 = VengefulList()
rs1.addLast(10)
rs1.addLast(11)
rs1.addLast(12)
rs1.addLast(13)
rs1.removeLast()
rs1.removeLast()
rs1.printLostItems()

# rotateRight(rs1)
# rs1.iterativeDisplay()