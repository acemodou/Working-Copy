class DoubleHashing:
    def __init__(self, size) -> None:
        self.size = size
        self.hash_table = [None] * (self.size * 2)
    
    def hash_function(self, key) -> int:
        return sum(ord(char) for char in key) % self.size
    
    def double_hashing(self, index, key) -> int:
        h2_value = sum(ord(char) for char in key) % 7
        return (index + 7 - h2_value) % self.size

    def probe(self, idx, key) -> int:
        idx1 = self.double_hashing(idx, key)
        i = 0
        while self.hash_table[(idx + i * idx1) % (self.size * 2)] is not None:
            i += 1
        return (idx + i * idx1) % (self.size * 2)

    def insert(self, key, value) -> None:
        idx = self.hash_function(key)

        while self.hash_table[idx] is not None:
            idx = self.probe(idx, key)
        self.hash_table[idx] = (key, value)

    def search(self, key) -> int or None:
        idx = self.hash_function(key)
        idx1 = self.double_hashing(idx, key)
        i = 0

        while self.hash_table[(idx + i * idx1) % (self.size * 2)] is not None:
            if self.hash_table[(idx + i * idx1)][0] == key:
                return self.hash_table[(idx + i * idx1) % (self.size * 2)][1]
            i += 1
        return None

    def delete(self, key) -> int or None:
        idx = self.hash_function(key)
        idx1 = self.double_hashing(idx, key)
        i = 0

        while self.hash_table[(idx + i * idx1) % (self.size * 2)] is not None:
            if self.hash_table[(idx + i * idx1)][0] == key:
                deleted_value = self.hash_table[(idx + i * idx1) % (self.size * 2)][1]
                self.hash_table[(idx + i * idx1) % (self.size * 2)] = None
                return deleted_value
            i += 1
        return None

# Example usage:
double_hashing_hash_table = DoubleHashing(3)
double_hashing_hash_table.insert("A", 42)
double_hashing_hash_table.insert("B", 30)
double_hashing_hash_table.insert("K", 60)

result = double_hashing_hash_table.search("A")
print(result)  # Output: 42

deleted_value = double_hashing_hash_table.delete("K")
print(deleted_value)  # Output: 60
