class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None 

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head is None 
    
    def delete(self):
        val = self.head.value  
        self.head = self.head.next
        return val
    
    def sorted_insert(self, key):
        """
        If there is no head we  or the new  value is smaller than head we set is as head 
        otherwise we have a ptr and a tail ptr and insert in between 
        """
        new_node = Node(key)
        if not self.head or key < self.head.value:
            new_node.next = self.head 
            self.head = new_node 
            return
    
        curr_ptr = self.head.next 
        prev_ptr = self.head
        while curr_ptr and key > curr_ptr.value:
            prev_ptr = curr_ptr 
            curr_ptr = curr_ptr.next 

        prev_ptr.next = new_node
        new_node.next = curr_ptr

    def search(self, key):
        curr_ptr = self.head 
        while curr_ptr:
            if curr_ptr.value == key:
                return True
            curr_ptr = curr_ptr.next  
        return False  

def hash_function(key):
    return key % 10 

def chaining(values):
    hash_table = [SinglyLinkedList() for _ in range(10)]
    for value in values:
        hash_table[hash_function(value)].sorted_insert(value)
    return hash_table

def search(linkedlist, key):
    idx = hash_function(key)
    if linkedlist[idx].isEmpty():
           return False 
    return linkedlist[idx].search(key)

