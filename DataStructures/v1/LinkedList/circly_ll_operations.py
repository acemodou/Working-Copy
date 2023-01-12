'''
Brief:
    Script for singly linked list operations
Author(s):
    Modou Jaw
'''

class Node:
    ''' This mimics a node structure '''
    def __init__(self, data):
        self.data = data 
        self.next = None  

class CircularLinkedList:
    ''' This links point to our next node '''
    def __init__(self):
        self.head = None 
    
    def prepend(self, ele):
        ''' This add a new node to the front '''
        newNode = Node(ele)
        newNode.next = self.head 

        if not self.head: 
            newNode.next = newNode
 
        else:
            ptr = self.head
            while ptr.next != self.head:
                ptr = ptr.next 
            ptr.next = newNode 
        self.head = newNode
        return newNode.data
    
    def append(self, ele):
        ''' Adds a new node to the back '''
        newNode = Node(ele)
        
        if not self.head:
            self.head = newNode
            newNode.next = self.head 
        else:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = newNode
            newNode.next = self.head 
        return newNode.data 

    def display(self):
        ''' Showing the content of our list '''
        curr = self.head 
        strs = ""
        while curr:
            strs += str(curr.data) + '-->'
            if curr.next == self.head:
                break
            curr = curr.next 
        return strs + 'Head'
    
    def recursive_display(self, ptr):
        ''' Recursively show the content of our list '''
        self.strs = ""
        def display(ptr):
            if ptr.next != self.head:
                self.strs += str(ptr.data) + '-->'
                display(ptr.next)
            else:
                self.strs += ptr.data + '-->'
            return self.strs + 'Head'
        return display(ptr)
    
    def remove(self, key):
        ''' Removing a node from the list '''
        curr = self.head 
        if self.head.data == key:
            while curr.next != self.head:
                curr = curr.next 
            curr.next = self.head.next 
            self.head = self.head.next 
            return self.display()
        else:
            prev = None 
            while curr.next != self.head:
                prev = curr 
                curr = curr.next 
                if curr.data == key:
                    prev.next = curr.next 
                    curr = curr.next 
                    return self.display()
        
        return f'{key} is not in our list '
    
    def remove_node(self, node):
        ''' Removing a node from the list '''
        curr = self.head 
        if self.head == node:
            while curr.next != self.head:
                curr = curr.next 
            curr.next = self.head.next 
            self.head = self.head.next 
            return self.display()
        else:
            prev = None 
            while curr.next != self.head:
                prev = curr 
                curr = curr.next 
                if curr == node:
                    prev.next = curr.next 
                    curr = curr.next 
                    return self.display()
        
        return f'{node} is not in our list '
    def __len__(self):
        ''' Override python len '''
        curr = self.head 
        count = 0
        while curr:
            count += 1
            curr = curr.next
            if curr == self.head:
                break 
        return count 
  
    def split_list(self):
        ''' Split the list in two halves '''
        size = len(self)
        if size == 0:
            return " We can't split and empty list"
        if size == 1:
            return self.head.data 
        else:
            mid = size // 2
            count = 0 
            curr = self.head 
            prev = None 
            while count < mid:
                count += 1 
                prev = curr 
                curr = curr.next
            prev.next = self.head 

            split_list = CircularLinkedList()
            while curr.next != self.head:
                split_list.append(curr.data)
                curr = curr.next 
            split_list.append(curr.data)

        return (self.display(), split_list.display())
    
    def josephus(self, node, step):
        ''' https://www.youtube.com/watch?v=uCsD3ZGzMgE&ab_channel=Numberphile '''

        curr =  self.head 
        while len(self) > 1:
            count = 1
            while count != step:
                count += 1
                curr = curr.next 
            print(f'Killing: {curr.data}')
            self.remove_node(curr)
            curr = curr.next 
        return self.display()

    def is_circular_list(self, input_list):
        ''' Checking if its a loop or sequential'''
        curr = input_list.head 
        while curr.next:
            curr = curr.next 
            if curr.next == input_list.head:
                return True
        return False 
    
    def is_loop(self):
        ''' We are checking if a loop is detected by having a pointer
         move faster than another'''
        
        p = self.head
        q = self.head 
        while p and q:
            p = p.next 
            q = q.next.next 
            if p == q:
                return True 
        return False 






        




         

        
    


