'''
Brief:
    Script for circular double linked list
Author(s):
        Modou Jaw
'''

class Node:
    '''This class mimics the node structure '''
    def __init__(self, data):
        ''' Initialize our node structure '''
        self.prev = None
        self.data = data  
        self.next = None  
        

class CircularDoubleLinkedList:
    ''' This is the linked list that linked our elements '''
    
    def __init__(self):
        ''' Setting up our head '''
        self.head = None 

    def append(self, ele):
        ''' This adds a new element at the end '''
        new_node = Node(ele)
        if not self.head:
            self.head = new_node
            self.head.next = self.head 
            return new_node.data 
        else:
            curr = self.head 
            while curr.next != self.head:
                curr = curr.next 
            curr.next = new_node
            new_node.prev = curr 
            new_node.next = self.head 
            return new_node.data 

    def display(self):
        ''' This shows the elements in our list '''
        strs = ""
        curr = self.head
        while curr.next != self.head:
            strs += str(curr.data) + "-->" 
            curr = curr.next
        return f"None-->{strs}{curr.data}-->None" 
    
    def add_after_node(self, key, ele):
        ''' We add a node after a specific key '''
        # Assume there is at least a node
        if not self.head:
            raise "There is no node "
        new_node = Node(ele)
        curr_ptr = self.head 
        while curr_ptr.next != self.head:
            if key == curr_ptr.data:
                new_node.next = curr_ptr.next 
                new_node.prev = curr_ptr
                curr_ptr.next = new_node
                new_node.next.prev = new_node
                return self.display()
            else:
                curr_ptr = curr_ptr.next  


    
    def insert(self, ele, index):
        ''' Insert a node at a given position '''
        pass 

       

    def add_before_node(self, key, ele):
        ''' We add a node before a specific key '''
        pass 
        
    
    def delete(self, ele):
        ''' Delete any element in a single list '''
        pass 
        

    def reverse(self):
        ''' Reverse the list '''
        pass 
        
    def delete_node(self, node):
        ''' Delete any element in a single list '''
        pass 
        

    def remove_dup(self):
        ''' Remove duplicates with the help of a dictionary '''
        pass 
        
    
    def pairs_with_sum(self, sum_value):
        ''' Check what two pairs sums up to a value '''
        pass 
        

    def convert_array_to_linked_list(self, A):
        ''' Convert the array as linked list '''
        pass 
        
    
    def delete_at_index(self, index):
        ''' Remove a node from a given index '''
        pass 
        





