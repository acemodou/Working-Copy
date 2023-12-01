# This is an input class. Do not edit.
   

def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
    
    newLinkedList = LinkedList(0)
    currList = newLinkedList 
    listOne = linkedListOne
    listTwo = linkedListTwo
    carry = 0 
    while listOne or listTwo or carry != 0:
        valueOne = listOne.value if listOne else 0 
        valueTwo = listTwo.value if listTwo else 0
        
        sumOfNodes = (valueOne + valueTwo + carry) 
        result = sumOfNodes % 10
        newNode = LinkedList(result)
        currList.next = newNode
        currList = newNode 
        carry = sumOfNodes // 10 
        listOne = listOne.next if listOne else None
        listTwo = listTwo.next if listTwo else None
    return newLinkedList.next 

def mergingLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
  
    listOne = linkedListOne
    listTwo = linkedListTwo
    
    while listOne is not listTwo:
        if not listOne:
            listOne = linkedListTwo
        else:
            listOne = listOne.next
        
        if not listTwo:
            listTwo = linkedListOne
        else:
            listTwo = listTwo.next
    return listOne 

def mergingLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
  
    listOne = linkedListOne
    listTwo = linkedListTwo
    
    listOneLength = getLength(listOne)
    listTwoLength = getLength(listTwo)
    
    diff = abs(listOneLength - listTwoLength)
    
    biggerNode = listOne if listOneLength > listTwoLength else listTwo
    smallerNode = listTwo if listOneLength > listTwoLength else listOne
    
    for _ in range(diff):
        biggerNode = biggerNode.next 
    
    while biggerNode is not smallerNode:
        biggerNode = biggerNode.next
        smallerNode = smallerNode.next 
    return biggerNode

def getLength(head):
    if head.next == None:
        return 1
    return 1 + getLength(head.next)

def mergingLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
    listOneNodes = set()
    listOne = linkedListOne
    while listOne:
        listOneNodes.add(listOne)
        listOne = listOne.next 
    
    listTwo = linkedListTwo
    while listTwo:
        if listTwo in listOneNodes:
            return listTwo
        listTwo = listTwo.next 
    return None

L1 = LinkedList(2)
L1.addMany([4,7,1])
L2 = LinkedList(9)
L2.addMany([4,5])
# sumOfLinkedLists(L1, L2)