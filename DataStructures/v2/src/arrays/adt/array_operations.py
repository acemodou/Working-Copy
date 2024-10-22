from array_interface import ArrayInterface

class ArrayOperations(ArrayInterface):
    def __init__(self, size) -> None:
        self.size = size 
        self.length = 0
        self.array = [0] * size 
        
    def validate_boundary(self, index):
         if self.length == self.size or self.size < index >= 0:
            raise IndexError(f"Out of range") 
        
    def append_element(self, value):
        if self.length < self.size:
            self.array[self.length] = value
            self.length += 1
        else:
            raise IndexError(f"Out of range, we can't exceed {self.size}")
    
    def insert_element(self, index, value):
        self.validate_boundary(index)
        
        idx = self.length
        while idx > index:
            self.array[idx] = self.array[idx-1]
            idx -= 1 
        self.array[index] = value 
        self.length += 1 
            
 
    def delete_element(self, index):
        self.validate_boundary(index)
        
        for i in range(index, self.length):
            self.array[i] = self.array[i+1]
        self.length -= 1 
        
    def get_index(self, index):
        self.validate_boundary(index)
        return self.array[index]
    
    def set_index(self, index, value):
        self.validate_boundary(index)
        self.array[index] = value
        self.length += 1
        
    def display(self):
        print(self.array)
    
    def search(self, value):
        for val in self.array:
            if val == value:
                print(f"{value} found in the array")
                return 
        print(f"{value} not found in the array!")
    
    def left_shift(self):
        shifted_value = self.array[0]
        for i in range(self.length -1):
            self.array[i] = self.array[i+1]
        self.array[self.length-1] = shifted_value
        


op = ArrayOperations(10)
op.append_element(8)
op.append_element(3)
op.append_element(7)
op.append_element(12)
op.append_element(6)
op.append_element(9)
op.append_element(10)
op.insert_element(4, 15)
op.delete_element(1)
op.search(15)
#print(op.get_index(5))
#op.set_index(8, 13)
op.left_shift()
op.display()

        