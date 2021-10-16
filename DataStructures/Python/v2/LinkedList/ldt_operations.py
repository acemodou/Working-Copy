from typing import Counter


class Node:
    ''' Linked List Structure '''
    def __init__(self):
        self.data = None
        self.next = None 
    
# Create and handle list operation 
class SLinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, ele):
        new_node = Node()
        new_node.data = ele 
        new_node.next = self.head
        self.head = new_node
    
    def display(self):
        ptr = self.head
        while ptr != None:
            print(ptr.data, end=' ')
            ptr = ptr.next
    
    def insertAtPosition(self, index, ele):
        new_node = Node()
        new_node.data = ele 
        ptr = self.head 

        if index == 0 and self.count(ptr):
            new_node.next = self.head 
            self.head = new_node

        else:
            for _ in range(index-1):
                ptr = ptr.next 
            new_node.next = ptr.next 
            ptr.next = new_node

    def count(self, ptr):
        ptr = self.head
        counter = 0
        while ptr != None:
            counter += 1
            ptr = ptr.next
        return counter 

    def sum(self, ptr):
        sum_nodes = 0
        ptr = self.head 
        while ptr != None:
            sum_nodes += ptr.data
            ptr = ptr.next 
        return sum_nodes
    
    def maxim(self, ptr):
        ptr = self.head 
        maxs = float('-inf')
        while ptr != None:
            if ptr.data > maxs:
                maxs = ptr.data
            ptr = ptr.next 
        return maxs 

    def LSearch(self, ptr, key):
        ptr = self.head
        index = 0
        while ptr != None:
            if ptr.data == key:
                print(f'Key found at index: {index}')
                return 
            ptr = ptr.next
            index += 1 
    
    def moveToFront(self, ptr, key):
        ptr = self.head 
        tail_ptr = ptr   
        index = 0 
        while ptr != None:
            if key == ptr.data:
                print(f'Improve Search Key found at index: {index}')
                tail_ptr.next = ptr.next 
                ptr.next = self.head 
                self.head = ptr  
            tail_ptr = ptr 
            ptr = ptr.next 
            index += 1 

if __name__ == "__main__":
    ll = SLinkedList()

    ll.insert(6)
    ll.insert(7)
    ll.insert(9)
    ll.insert(3)
    ll.insert(8)

    ll.insertAtPosition(0,11) 
    ll.insertAtPosition(3,4)
    print(f'The length is: {ll.count(ll)}')
    ll.display()
    print(f'\nSum of nodes is: {ll.sum(ll)}')
    print(f'The maximum element in our data is: {ll.maxim(ll)}')
    ll.LSearch(ll, 6)
    ll.moveToFront(ll, 9)
    ll.display()