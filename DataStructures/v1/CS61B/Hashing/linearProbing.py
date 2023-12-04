class LinearProbingHashTable:
    def __init__(self, size) -> None:
        self.size = size 
        self.hash_table = [None] * (size * 2) 

    
    def hash_function(self, key) -> int:
        # Don't understand how python implemented it's hash function. Need to look at it before using it.
        # Commenting this for now
        #return hash(key) % self.size
        return sum(ord(char) for char in key) % self.size
    
    def probe(self, hash_code) -> int:
        """
        Checking for the next empty space to insert a value
        """
        i = 0
        while self.hash_table[(hash_code + i) % (self.size * 2)] != None:
            i += 1
        return (hash_code + i) % (self.size * 2)

    def insert(self, key, value) -> None:
        idx = self.hash_function(key)

        while self.hash_table[idx] != None:
            idx = self.probe(idx)
        self.hash_table[idx] = (key, value)
        

    def search(self, key) -> int:
        idx = self.hash_function(key)
        print(self.hash_table[idx][0])

        while self.hash_table[idx][0] != key and self.hash_table[idx] != None:
            idx += 1
        print(self.hash_table[idx][1])
        return self.hash_table[idx][1]

    def delete(self, key) ->int:
        """
        In linear probing we don't want to delete because if we delete we have to 
        reinsert all the values and put them back. We won't implement delete
        """
        
    

linear_probing_hash_table = LinearProbingHashTable(2)
linear_probing_hash_table.insert("A", 42)
linear_probing_hash_table.insert("B", 30)
linear_probing_hash_table.insert("K", 60)

linear_probing_hash_table.search("A")