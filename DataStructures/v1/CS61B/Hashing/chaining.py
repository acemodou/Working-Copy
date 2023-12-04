class Node:
    def __init__(self, key, value) -> None:
        self.key = key 
        self.value = value 
        self.next = None  

class ChaniningHashTable:
    def __init__(self, size) -> None:
        self.size = size 
        self.hash_table = [None] * size
    
    def hash_function(self, input_data) -> int:
        return sum(ord(char) for char in input_data) % 10 if type(input_data) is str else input_data % 10 

    def insert(self, key, value, insert_key_or_value = True) -> Node:
        hash_key = key if insert_key_or_value else value
        idx = self.hash_function(hash_key)
        new_node = Node(key, value)

        if self.hash_table[idx] is None:
            new_node.next = self.hash_table[idx]
            self.hash_table[idx] = new_node

        else:
            current_node = self.hash_table[idx]
            prev = None 
            while current_node is not None and current_node.value < value:
                prev = current_node
                current_node = current_node.next
            
            if prev is None:
                new_node.next = current_node
                self.hash_table[idx] = new_node
            else:
                prev.next = new_node
                new_node.next = current_node

    def search(self, key_or_value, search_by_key = True) -> int or str:
        idx = self.hash_function(key_or_value)
        curr_ptr = self.hash_table[idx]

        while curr_ptr is not None:
            if (search_by_key and curr_ptr.key == key_or_value) or (not search_by_key and curr_ptr.value == key_or_value):
                return curr_ptr.value if search_by_key else curr_ptr.key
            curr_ptr = curr_ptr.next
       
        return f"{key_or_value} is not in our dictionary"
    
    def delete(self, key_or_value, search_by_key = True) -> int or str:
        idx = self.hash_function(key_or_value)
        curr_node = self.hash_table[idx]
        prev = None
        
        if curr_node is None:
            return f'{key_or_value} is not in our dictionary!'

        while curr_node is not None and (search_by_key and curr_node.key != key_or_value) or (not search_by_key and curr_node.value != key_or_value):
            prev = curr_node
            curr_node = curr_node.next 
        if curr_node is not None:
            if prev is None:
                self.hash_table[idx] = curr_node.next 
            else:
                prev.next = curr_node.next



hash_table = ChaniningHashTable(size = 10)
hash_table.insert("A", 42, insert_key_or_value=True)
hash_table.insert("B", 30, insert_key_or_value=True)

# Search by key
result = hash_table.search("A", search_by_key=True)
print(result)  # Output: 42

# Search by value
result = hash_table.search("B", search_by_key=True)
print(result)  # Output: 30

# Delete by key
hash_table.delete("A", search_by_key=True)

# Delete by value
hash_table.delete(30, search_by_key=False)