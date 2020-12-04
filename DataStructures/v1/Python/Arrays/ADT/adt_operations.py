class ADT:
    def __init__(self, size, length):
        self.size = size
        self.length = length
        self.arr = []
    
    def initialize(self):
        '''
        initializing entire array to 0
        return the array 
        '''
        self.arr = [0 for _ in range(self.size)]
        return self.arr 

    def Display(self):
        print(f"Displaying the elements in {self.arr}")
        for i in range(self.length):
            print(f'Elements are: {i} : {self.arr[i]}')
    
    def Append(self, x):
        '''
        We are adding an element at the end of a list
        Check if there is available space to add a new element
        Increment the length anytime we add a new element
        '''
        if self.length < self.size:
            self.arr[self.length] = x
            self.length +=1
    
    def Insert(self, index, element):
        '''
        Check if the given index is valid 
        Check if there is available space to add a new element
        Increment the length anytime we add a new element
        Need to understand and fix insert properly
        '''
        if index >=0 and index <= self.length and self.length <= self.size:
            for i in range(self.length, index-1, -1):
                self.arr[i+1] = self.arr[i]
            self.arr[index] = element
            self.length +=1

       
    
    

        
