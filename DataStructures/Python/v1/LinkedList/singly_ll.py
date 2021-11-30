from typing import NewType


class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class singly_list:
    def __init__(self):
        self.head = None 

    def display_list(self):
        ptr = self.head
        ll_str = '' 
        while ptr:
            ll_str += str(ptr.data) + '--> '
            ptr = ptr.next 
        print(ll_str)

    def Append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        last_ptr = self.head 
        while last_ptr.next:
            last_ptr = last_ptr.next 
        last_ptr.next = new_node
    
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head 
        self.head = new_node
    
    def insert_at_position(self, index, data):
        new_node = Node(data)
        ptr = self.head 

        if index == 0:
            new_node.next = self.head 
            self.head = new_node
            return 
        else:
            for _ in range(index-1):
                ptr = ptr.next 
            new_node.next = ptr.next 
            ptr.next = new_node 

    def delete(self, key):
        # Check if the key is the head node and if there is a head
        # advance the head and set the current node to None
        curr_node = self.head
        if curr_node and curr_node.data == key:
            self.head = self.head.next 
            curr_node = None
            return  
        
        prev = None
        while curr_node and curr_node.data != key:
            prev = curr_node
            curr_node = curr_node.next
        
        if not curr_node:
            raise('We are out of bounds !!!')

        prev.next = curr_node.next 
        curr_node = None 
    
    def delete_at_index(self, index):
        curr_node = self.head 
        if index == 0:
            self.head = self.head.next 
            curr_node = None 
            return 
        
        prev = None 
        for _ in range(index):
            prev = curr_node
            curr_node = curr_node.next 
        
        if not curr_node:
            raise("We are not handling out of bounds")

        prev.next = curr_node.next 
        curr_node = None 

    def get_len(self):
        curr_node = self.head 
        count = 0 
        while curr_node: 
            count += 1
            curr_node = curr_node.next 
        return count
    
    def get_len_recurs(self, head):
        if head is None:
            return 0
        return 1 + self.get_len_recurs(head.next)

    def swap_nodes(self, key1, key2):
        if key1 == key2:
            return
        
        curr_1 = self.head 
        prev_1 = None 
        while curr_1 and curr_1.data != key1:
            prev_1 = curr_1
            curr_1 = curr_1.next
        
        curr_2 = self.head 
        prev_2 = None 
        while curr_2 and curr_2.data != key2:
            prev_2 = curr_2
            curr_2 = curr_2.next

        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2
        
        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1
        
        curr_1.next, curr_2.next = curr_2.next, curr_1.next 



sl = singly_list()
sl.Append(1)
sl.Append(2)
sl.Append(3)
sl.prepend(5)

# sl.insert_at_position(2, 0)
# sl.delete(3)
# sl.delete_at_index(4)
# print(sl.get_len())
# print(sl.get_len_recurs(sl.head))

sl.swap_nodes(5, 3)
sl.display_list()
