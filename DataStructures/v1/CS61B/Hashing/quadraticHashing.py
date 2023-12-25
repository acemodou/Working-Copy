class QuadraticHashTable:
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
        while self.hash_table[(hash_code + (i*i)) % (self.size * 2)] != None:
            i += 1
        return (hash_code + (i*i)) % (self.size * 2)

    def insert(self, key, value) -> None:
        idx = self.hash_function(key)
  
        while self.hash_table[idx] != None:
            idx = self.probe(idx)
        self.hash_table[idx] = (key, value)
        

    def search(self, key) -> int:
        idx = self.hash_function(key)
        i = 0
        while self.hash_table[idx + (i * i)] is not None and self.hash_table[idx + (i * i)][0] != key:
            i += 1

        if self.hash_table[idx + (i * i)] is not None:
            return self.hash_table[idx + (i * i)][1]
        else:
            print(f'{key} not found!')
            return None


    def delete(self, key) ->int:
        idx = self.hash_function(key)
        i = 0 
        while self.hash_table[idx + (i * i)] != None:
            if self.hash_table[idx + (i * i)][0] == key:
                x = self.hash_table[idx + (i*i)][1]
                self.hash_table[idx + (i * i)]  = None 
                return x 
            i += 1
        return f'{key} not found!'


linear_probing_hash_table = QuadraticHashTable(3)
linear_probing_hash_table.insert("A", 42)
linear_probing_hash_table.insert("B", 30)
linear_probing_hash_table.insert("K", 60)


linear_probing_hash_table.delete("K")
linear_probing_hash_table.search("K")