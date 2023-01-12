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

class SinglyLinkedList:
    ''' This links point to our next node '''
    def __init__(self):
        self.head = None

    def prepend(self, ele):
        ''' This add a new node at the first position'''
        newNode = Node(ele)
        newNode.next = self.head
        self.head = newNode
        return newNode.data 

    def insert(self, index, ele):
        ''' Insert at any giving valid position '''
         # TODO: Check if we have a valid length after implement get_length
        if index < 0 or index > self.get_length():
            raise("We are out of boundaries")
        newNode = Node(ele)
        if index == 0:
            newNode.next = self.head 
            self.head = newNode
        
        else:
            ptr = self.head 
            for _ in range(index - 1):
                ptr  = ptr.next 
            newNode.next = ptr.next 
            ptr.next = newNode
            return newNode.data
    
    def append(self, ele):
        ''' Insert at the end '''
        newNode = Node(ele)
        newNode.next = None 

        if not self.head:
            ''' New node is the head node '''
            self.head = newNode
        else:
            ptr = self.head 
            while ptr.next:
                ptr = ptr.next 
            ptr.next = newNode
    
    def display(self):
        ''' Display linked list '''
        ptr = self.head 
        ll_strs = ''
        while ptr:
            ll_strs += str(ptr.data) + '-->'
            ptr = ptr.next
        return ll_strs + "None" 

    def recursive_display(self, head):
        ''' Recursively display linked list '''
        if head:
            print(head.data, end=' ')
            self.recursive_display(head.next)
    
    def get_length(self):
        ''' Get the length of the linked list '''
        ptr = self.head 
        count = 0
        while ptr:
            count += 1
            ptr = ptr.next
        return count 
    
    def recursive_get_length(self, ptr):
        ''' Recursively get the length'''
        if not ptr:
            return 0
        return 1 + self.recursive_get_length(ptr.next) 
    
    def sum(self):
        ''' Sum the elements in a singly list'''
        ptr = self.head 
        sum = 0
        while ptr:
            sum += ptr.data 
            ptr = ptr.next
        return sum 
    
    def recursive_sum(self, ptr):
        ''' Recursively get the elements in a list'''
        if not ptr:
            return 0
        return ptr.data + self.recursive_sum(ptr.next)
    
    def max(self):
        ''' Return the max element in a list '''
        max_ele = float("-inf")
        ptr = self.head 
        while ptr:
            if ptr.data > max_ele:
                max_ele = ptr.data 
            ptr = ptr.next 
        return max_ele
    
    def recursive_max(self, ptr):
        ''' Return the max element recursively'''
        x = 0
        if not ptr:
            return float("-inf")
        x = self.recursive_max(ptr.next)
        return x if ptr.data < x else ptr.data
    
    def linear_search(self, key):
        ''' Search for and element in a list  '''
        ptr = self.head 
        while ptr:
            if ptr.data == key:
                return True 
            ptr = ptr.next 
        return False 
    
    def recursive_linear_search(self, ptr, key):
        ''' Sequential search recursively '''
        if not ptr:
            return False 
        
        if ptr.data == key:
            return True  
        return self.recursive_linear_search(ptr.next, key)
    
    def improve_linear_search(self, key):
        ''' Moving the search key to the front so that it 
            will be easily found the next time '''
        ptr = self.head 
        tail_ptr = None
        
        while ptr:
            if ptr.data == key:
                tail_ptr.next = ptr.next 
                ptr.next = self.head 
                self.head = ptr 
            tail_ptr = ptr 
            ptr = ptr.next 
        return self.display()
    
    def insert_in_sorted_list(self, ele):
        ''' Inserting and element in a sorted list '''
        
        temp = Node(ele)
        ptr = self.head
        tail_ptr = None
        
        ''' Check if there is no node'''
        if not self.head:
            self.head = temp

        if self.head.data > ele:
           
            temp.next = self.head 
            self.head = temp
            return self.display()
        
        while ptr and ptr.data < ele:
            tail_ptr = ptr 
            ptr = ptr.next 
        temp.next = tail_ptr.next 
        tail_ptr.next = temp 
        return self.display()
    
    def delete(self, index):
        ''' Removing a node at a given index '''
        ptr = self.head
        prev = None 
        if index == 0:
            self.head = self.head.next
            deletedEle = ptr.data 
            ptr = None 
            return deletedEle
        else:
            for _ in range(index - 1):
                prev = ptr 
                ptr = ptr.next
            if not ptr:
                raise('We are out of bound')
            prev.next = ptr.next 
            deletedEle = ptr.data 
            ptr = None 
            return deletedEle
    
    def is_sorted(self):
        ''' Checking if a list is sorted '''
        # Method 1
        # prev = self.head 
        # curr = self.head.next 
        # while curr:
        #     if curr.data < prev.data:
        #         return "Is not sorted"
        #     prev = curr 
        #     curr = curr.next 
        # return "Is sorted"

        curr = self.head 
        ele = float("-inf")
        while curr:
            if curr.data < ele:
                return "Is not sorted"
            ele = curr.data 
            curr = curr.next 
        return "Is sorted"
    
    def remove_dup(self):
        ''' Remove duplicates in a sorted list '''
        curr = self.head.next 
        prev = self.head 
        while curr:
            if curr.data != prev.data:
                prev = curr 
                curr = curr.next 
            else:
                prev.next = curr.next 
                curr = None 
                curr = prev.next 
        return self.display()
    
    def reverse_elements(self):
        ''' Reverse a linked list using auxiliary array '''
        array = [0] * self.get_length()
        curr = self.head
        idx = 0
        while curr:
            array[idx] = curr.data 
            idx += 1
            curr = curr.next 
        idx -= 1
        curr = self.head
        while curr:
            curr.data = array[idx]
            idx -=1
            curr = curr.next 
        return self.display()

    def reverse_links(self):
        ''' Reverse a linked list with sliding pointers '''
        curr = self.head 
        p = None 
        q = None 
        while curr:
            p = q 
            q = curr
            curr = curr.next 
            q.next = p
            
        self.head = q 
        return self.display()

    def recursive_reverse_links(self, tail, head):
        ''' Recursive reverse linked linked using head recursion '''
        if head:
            self.recursive_reverse_links(head, head.next)
            head.next = tail
        else:
            self.head = tail 

    def concatenate(self, secondList):
        ''' Join two linked list together '''
        first = self.head 
        second = secondList.head 

        while first.next:
            first = first.next 
        first.next = second 
        second = None 
        return self.display()  

    def merge_sorted_lists(self, secondList):
        ''' Merge two sorted list together and return a final list '''
        first = self.head 
        second = secondList.head 
        final_head, curr = None, None 

        if first.data < second.data:
            final_head = first 
            curr = first
            first = first.next
            curr.next  = None 
        else:
            final_head = second 
            curr = second
            second = second.next 
            curr.next = None 
        while first and second:
            if first.data < second.data:
                curr.next = first 
                curr = first 
                first = first.next 
                curr.next = None 
            else:
                curr.next = second
                curr = second 
                second = second.next 
                curr.next = None 

        if first:
            curr.next = first 
        if second:
            curr.next = second
        
        return secondList.display()
    
    
class LinkedList:
    # Simplified version of linkedList 
    def __init__(self, value):
        self.value = value
        self.next = None
    def addMany(self, values):
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self

    def getNodesInArray(self):
        nodes = []
        current = self
        while current is not None:
            nodes.append(current.value)
            current = current.next
        return nodes
test = LinkedList(1).addMany([1,3, 4, 4, 4, 5, 6, 6])
test.getNodesInArray()
