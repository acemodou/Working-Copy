'''
Brief:
    Script for doubly linked list
Author(s):
        Modou Jaw
'''


class Node:
    '''This class mimics the node structure '''
    def __init__(self, data):
        ''' Initialize our node structure '''
        self.data = data 
        self.prev = None 
        self.next = None 

class DoubleLinkedList:
    ''' This is the linked list that linked our elements '''
    
    def __init__(self):
        ''' Setting up our head '''
        self.head = None 

    def append(self, ele):
        ''' This adds a new element at the end '''
        newNode = Node(ele)
        if not self.head:
            newNode.prev = None 
            self.head = newNode
            return newNode.data 
        
        else:
            curr = self.head 
            while curr.next:
                curr = curr.next 
            curr.next = newNode
            newNode.prev = curr
            newNode.next = None 
            return newNode.data 

    def prepend(self, ele):
        ''' This adds a new element at the front of our node '''
        newNode = Node(ele)
        if not self.head:
            newNode.prev = None 
            self.head = newNode
            return newNode.data 
        else:
            newNode.next = self.head 
            self.head.prev = newNode
            self.head = newNode
            newNode.prev = None 
            return newNode.data
    
    def display(self):
        ''' This shows the elements in our list '''
        strs = ""
        curr = self.head 
        while curr:
            strs += str(curr.data) + '-->'
            curr = curr.next 
        return f'None-->{strs}None' 
    
    def add_after_node(self, key, ele):
        ''' We add a node after a specific key '''
        curr = self.head 
        while curr:
            if curr.data == key and curr.next is None:
                self.append(ele)
            elif curr.data == key:
                newNode = Node(ele)
                next_ptr = curr.next 
                curr.next = newNode
                newNode.next = next_ptr
                newNode.prev = curr 
                next_ptr.prev = newNode
            curr = curr.next
        return self.display()
    
    def insert(self, ele, index):
        ''' Insert a node at a given position '''

        new_node = Node(ele)
        if index == 0:
            new_node.next = self.head 
            self.head.prev = new_node
            new_node.prev = None 
            self.head = new_node
            return self.display()
        
        else:
            ptr = self.head 
            for _ in range(index -1):
                ptr = ptr.next 
            new_node.next = ptr.next 
            new_node.prev = ptr 
            if ptr:
                ptr.next.prev = new_node
                ptr.next = new_node
            return self.display()

    def add_before_node(self, key, ele):
        ''' We add a node before a specific key '''
        curr = self.head 
        while curr:
            if curr.data == key and curr.prev is None:
                self.prepend(ele)
            elif curr.data == key:
                newNode = Node(ele)
                pre_ptr = curr.prev 
                curr.prev = newNode 
                newNode.prev = pre_ptr 
                pre_ptr.next = newNode
                newNode.next = curr 
            curr = curr.next 
        return self.display()
    
    def delete(self, ele):
        ''' Delete any element in a single list '''
        curr = self.head 
        while curr:
            #  Deleting head node 
            if curr.data == ele and curr == self.head:
                # case 1: Head is the only element
                if not curr.next:
                    curr = None 
                    self.head = None
                    return self.display()

                # Case 2: Head isn't the only element 
                else:
                    next_ptr = curr.next 
                    curr.next = None 
                    next_ptr.prev = None 
                    curr = None 
                    self.head = next_ptr
                    return self.display()

            # Case 3: Not deleting head node 
            elif curr.data == ele:
                if curr.next:
                    next_ptr = curr.next 
                    pre_ptr = curr.prev 
                    curr.next = None 
                    curr.prev = None 
                    curr = None 
                    pre_ptr.next = next_ptr
                    next_ptr.prev = pre_ptr
                    return self.display()
                else:
                    # Case 4: Deleting the last node 
                    pre_ptr = curr.prev 
                    curr.next = None 
                    curr = None 
                    pre_ptr.next = None 
                    return self.display()
            curr = curr.next
        return self.display()

    def reverse(self):
        ''' Reverse the list '''
        curr = self.head 
        temp = None 
        while curr:
            temp = curr.prev
            curr.prev = curr.next 
            curr.next = temp 
            curr = curr.prev
            if curr and curr.next == None:
                self.head = curr 
        return self.display()
    
    def delete_node(self, node):
        ''' Delete any element in a single list '''
        curr = self.head 
        while curr:
            #  Deleting head node 
            if curr == node and curr == self.head:
                # case 1: Head is the only element
                if not curr.next:
                    curr = None 
                    self.head = None
                    return self.display()

                # Case 2: Head isn't the only element 
                else:
                    next_ptr = curr.next 
                    curr.next = None 
                    next_ptr.prev = None 
                    curr = None 
                    self.head = next_ptr
                    return self.display()

            # Case 3: Not deleting head node 
            elif curr == node:
                if curr.next:
                    next_ptr = curr.next 
                    pre_ptr = curr.prev 
                    curr.next = None 
                    curr.prev = None 
                    curr = None 
                    pre_ptr.next = next_ptr
                    next_ptr.prev = pre_ptr
                    return self.display()
                else:
                    # Case 3: Deleting the last node 
                    pre_ptr = curr.prev 
                    curr.next = None 
                    curr = None 
                    pre_ptr.next = None 
                    return self.display()
            curr = curr.next
        return self.display()

    def remove_dup(self):
        ''' Remove duplicates with the help of a dictionary '''
        curr = self.head 
        seen = dict()

        while curr:
            if curr.data not in seen:
                seen[curr.data] = 1
                curr = curr.next 
            else:
                next_ptr = curr.next 
                self.delete_node(curr)
                curr = next_ptr
        return self.display()
    
    def pairs_with_sum(self, sum_value):
        ''' Check what two pairs sums up to a value '''
        curr = self.head 
        after_curr = None
        pair_list = []
        while curr:
            after_curr = curr.next 
            while after_curr:
                if curr.data + after_curr.data == sum_value:
                    pair_list.append(f"{curr.data}, {after_curr.data}")
                after_curr = after_curr.next 
            curr = curr.next 
        
        return pair_list

    def convert_array_to_linked_list(self, A):
        ''' Convert the array as linked list '''
        new_node = Node(A[0])
        self.head = new_node
        new_node.prev = None 
        new_node.next = None 
        ptr = new_node 

        for i in range(1, len(A)):
            t = Node(A[i])
            t.next = ptr.next
            t.prev = ptr
            ptr.next = t
            ptr = t 
        return self.display()
    
    def delete_at_index(self, index):
        ''' Remove a node from a given index '''
        ptr = self.head
        if index == 1:
            self.head = self.head.next
            if self.head:
                self.head.prev = None 
            ptr = None
            return self.display() 
        else:
            for _ in range(index -1):
                ptr = ptr.next
            ptr.prev.next = ptr.next 
            if ptr.next:
                ptr.next.prev = ptr.prev
            ptr = None
            return self.display()





