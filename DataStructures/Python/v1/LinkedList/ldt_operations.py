
class Node:
    ''' Linked List Structure '''
    def __init__(self):
        self.data = None
        self.next = None 
    
# Create and handle list operation 
class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None # This is useful to create a second list 
    
    def insert(self, ele):
        new_node = Node()
        new_node.data = ele 
        new_node.next = self.head
        self.head = new_node
    
    def insert_2(self, ele):
        new_node = Node()
        new_node.data = ele 
        new_node.next = self.tail
        self.tail = new_node
    
    def display(self):
        ptr = self.head
        while ptr != None:
            print(ptr.data, end=' ')
            ptr = ptr.next
    
    def insertAtPosition(self, index, ele):
        new_node = Node()
        new_node.data = ele 
        ptr = self.head 

        if index == 1 and self.count(ptr):
            new_node.next = self.head 
            self.head = new_node

        else:
            for _ in range(index-1):
                ptr = ptr.next 
            new_node.next = ptr.next 
            ptr.next = new_node

    def deleteAtIndex(self, index):
         ptr = self.head
         tail_ptr = ptr 
         ele = -1

         if index == 1:
             ele = self.head.data
             self.head = self.head.next
             ptr = None
             return ele

         else:
             for _ in range(index -1):
                 tail_ptr = ptr
                 ptr = ptr.next
             tail_ptr.next = ptr.next
             ele = ptr.data
             ptr = None
             return ele  

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
    
    def insert_in_Sorted(self, ele):
        new_node = Node()
        new_node.data = ele 
        ptr = self.head
        tail_ptr = self.head 
        
        if self.head == None:
            self.head = new_node
        else:
            while ptr != None and ptr.data < ele:
                tail_ptr = ptr 
                ptr = ptr.next
            
            if ptr == self.head:
                new_node.next = self.head
                self.head = new_node
            else:
                new_node.next = tail_ptr.next
                tail_ptr.next = new_node
    
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
    
    def isSorted(self):
        ptr = self.head 
        ele = float("-inf")
        
        while ptr != None:
            if ptr.data < ele:
                return 0 
            ele = ptr.data 
            ptr = ptr.next 
        return 1
    
    def remove_duplicate(self):
        ''' This works in a sorted list '''
        ptr = self.head.next 
        tail_ptr = self.head 

        while ptr != None:
            if ptr.data != tail_ptr.data: 
                tail_ptr = ptr 
                ptr = ptr.next 
            else:
                tail_ptr.next = ptr.next 
                ptr = None
                ptr = tail_ptr.next
    
    def reverse_elements(self):
        ptr = self.head 
        q = ptr 
        i = 0 
        A = [0] * self.count(ptr)

        while q != None:
            A[i] = q.data 
            q = q.next 
            i += 1
        q = ptr 
        i -= 1

        while q != None:
            q.data = A[i]
            q = q.next 
            i -= 1

    def reverse_links(self):
        ''' Reversing the links to point backwards '''
        ptr = self.head 
        tail_ptr = None 
        q = None

        while ptr != None:
            tail_ptr = q 
            q = ptr 
            ptr = ptr.next 
            q.next = tail_ptr
        self.head = q
    
    def recursive_reverse(self, tail_ptr, ptr:Node):
       
        if ptr:
            self.recursive_reverse(ptr, ptr.next)
            ptr.next = tail_ptr
        else:
            self.head = tail_ptr
    
    def concatenate(self):
        ptr = self.head 
        while ptr.next != None:
            ptr = ptr.next 
        ptr.next = self.tail
    
    def merge(self):
        first = self.head 
        second = self.tail 
        last = None 

        if first.data < second.data:
            last = first 
            first = first.next 
            last.next = None  
        else:
            last = second
            second = second.next
            last.next = None 
        
        while first != None and second != None:
            if first.data < second.data:
                last.next = first 
                last = first 
                first = first.next 
                last.next = None  
            else:
                last.next = second
                last = second 
                second = second.next 
                last.next = None 

        if first != None:
            last.next = first
        if second != None:
            last.next = second 

    def is_loop(self):
        ptr = self.head 
        tail_ptr = self.head
        counter = 0
        while True:
            ptr = ptr.next
            while ptr != tail_ptr and counter !=self.count(ptr) and ptr != None:
                ptr = ptr.next.next 
                tail_ptr = tail_ptr.next
                counter += 1
                if ptr == tail_ptr:
                    return True 
            return False 
    
    def circular_node(self, A):
        first = Node()
        first.data = A[0]
        first.next = self.head 
        last = first 
        for i in range(1, len(A)):
            tail = Node()
            tail.data = A[i]
            tail.next = last.next 
            last.next = tail 
            last = tail  

    def display_circular(self):
        ptr  = self.head 
        flag = 0
        while ptr != self.head or flag == 0:
            flag = 1 
            print(ptr.data)
            ptr = ptr.next 




if __name__ == "__main__":
    ll = SLinkedList()
    A = [1,2,3,4,5]
    for i in A:
        ll.insert(i)
    ll.circular_node(A)
    ll.display_circular()
    # ll.insert(20)
    # ll.insert(15)
    # ll.insert(9)
    # ll.insert(7)
    # ll.insert(1)
    
    # print(ll.is_loop())
    # ll.insert(3)
    # ll.insert(3)
    # ll.insert(3)
    # ll.remove_duplicate()
    # ll.display()
    # print("\nReversing linked list ")
    # ll.reverse_elements()
    # ll.reverse_links()
    # ll.recursive_reverse(None, None)
    # import pdb 
    # pdb.set_trace()
    # ll.insert_2(62)
    # ll.insert_2(52)
    # ll.insert_2(42)
    # ll.insert_2(32)
    # ll.insert_2(22)
   
    
    # ll.merge()
    # ll.concatenate()
    ll.display()
    # ll.insertAtPosition(0,11) 
    # ll.insertAtPosition(3,4)
    # print(f'The length is: {ll.count(ll)}')
    # ll.display()
    # print(f'\nSum of nodes is: {ll.sum(ll)}')
    # print(f'The maximum element in our data is: {ll.maxim(ll)}')
    # ll.LSearch(ll, 6)
    # ll.moveToFront(ll, 9)
    # ll.insert_in_Sorted(100)
    # ll.deleteAtIndex(2)
    # print("\n")
    # ll.display()
    # if ll.isSorted():
    #     print("Sorted")
    # else:
    #     print("Not Sorted")