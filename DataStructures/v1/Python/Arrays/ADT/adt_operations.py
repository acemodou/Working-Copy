
class ADT:
    def __init__(self, size, length):
        self.size = size
        self.length = length
        self.arr = []
    
    def initialize(self):
        '''
        Filling the entire array with 0
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
        if self.length <= self.size:
            self.arr[self.length] = x
            self.length +=1
    
    def Insert(self, index, element):
        '''
        Check if the given index is valid 
        Check if there is available space to add a new element
        Increment the length anytime we add a new element
        '''
        if 0 <= index <= self.length <= self.size:
            for i in range(self.length, index, -1):
                self.arr[i] = self.arr[i-1]
            self.arr[index] = element
            self.length +=1
    
    def Delete(self, index):
        '''
        Deleting the index in an array
        Print the value deleted in that index
        '''
        x = self.arr[index]
        if 0 <= index <= self.length:
            for i in range(index, self.length, 1):
                self.arr[i] = self.arr[i+1]
            print(f'{x} deleted!')
            self.length -=1

    def LinearSearch(self, value):
        '''
        Search for a specific value and return a tuple(index, value found)
        Return "Value not found"
        '''
        for i in range(self.length):
            if self.arr[i] == value:
                return i, self.arr[i]
        return f'{value}: not in our list'
    
    def Transposition(self, value):
        '''
        This is an improved linear search
        We bring the value closer so that the next time we search, we will reduced a step
        This is only useful when we are not storing in main memory because everything will be lost once we done
        '''
        for i in range(self.length):
            if self.arr[i] == value:
                self.arr[i], self.arr[i-1] = self.arr[i-1], self.arr[i]
                return i, self.arr[i-1]
        return f'{value}: not in our list'
    
    def moveToFront(self, value):
        '''
        This is an improved linear search
        We bring the search value to the front so the next time we search it will be the first element
        This is only useful when we are not storing in main memory because everything will be lost once we done
        '''
        for i in range(self.length):
            if self.arr[i] == value:
                self.arr[i], self.arr[0] = self.arr[0], self.arr[i]
                return i, self.arr[0]
        return f'{value}: not in our list'
    
    def iterative_binary(self, value_search):
        left_side = 0
        right_side = self.length -1
        while left_side <= right_side:
            array_mid = (left_side + right_side) // 2
            if value_search == self.arr[array_mid]:
                return f"The value we are searching: {self.arr[array_mid]} is found in index:  {array_mid}"
            elif self.arr[array_mid] > value_search >= self.arr[left_side]:
                right_side = array_mid - 1
            elif self.arr[array_mid] < value_search <= self.arr[right_side]:
                left_side = array_mid + 1
            else:
                return f"The value we are searching {value_search}  does not exist. \n Exiting !!!"
                
    def recursive_binary(self, value_search,  left_side, right_side):

        array_mid = (left_side + right_side) // 2
        if value_search == arr[array_mid]:
            return array_mid, arr[array_mid]
        elif arr[array_mid] > value_search >= arr[left_side]:
            return recursive_binary(arr, value_search, left_side, array_mid - 1)
        elif arr[array_mid] < value_search <= arr[right_side]:
            return recursive_binary(arr, value_search, array_mid + 1, right_side)
        else:
            print(F"The value we are searching {value_search} does not exist. \n Exiting !!!")
            exit()

    def DeleteElement(self, value):
        '''
        This is an improved Delete
        We search the element and once is found we delete the index 
        '''
        for i in range(self.length):
            if self.arr[i] == value:
                self.Delete(i)
        return f'{value}: not in our list'
    
    def GetIndex(self, index):
        '''
        return the value at a specific index 
        '''
        if index >=0 and index <= self.length:
            return self.arr[index]
        
    def setIndex(self, index, value):
        '''
        Set value at a specific index 
        '''
        if index >=0 and index <= self.length:
            self.arr[index] = value
    
    def Min(self):
        '''
        Set min as the first element
        return mini 
        '''
        mini = self.arr[0]
        for i in range(self.length):
            if self.arr[i] < mini:
                mini = self.arr[i]
        return mini 
    
    def Max(self):
        '''
        Set Max as the first element in our array
        return mini
        '''
        maxi = self.arr[0]
        for i in range(self.length):
            if self.arr[i] > maxi:
                maxi = self.arr[i]
        return maxi 
    
    def Sum(self):
        total = 0
        for i in range(self.length):
            total += self.arr[i]
        return total 
    
    def ReverseArray(self):
        '''
        Create an auxiliary array
        Copy array to the auxiliary array in reverse order
        Copy the auxiliary array back to the array
        '''
        print("Reversing all elements".center(62, '-'))
        auxiliary_array = [0 for _ in range(self.length)]
        for i, j in zip(range(self.length -1, -1, -1), range(self.length)):
            auxiliary_array[j] = self.arr[i]
        for i in range(self.length):
            self.arr[i] = auxiliary_array[i]
    
    def ReverseArray_2(self):
        '''
        Swapping first element with last element
        Increament first index and decrement last index
        '''
        print("2ndReversing all elements".center(62, '-'))
        for i, j in zip(range(self.length), range(self.length -1, -1, -1)):
            # self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
            temp = self.arr[i]
            self.arr[i] = self.arr[j]
            self.arr[j] = temp 
    
    def LeftShift(self):
        '''
        We shift all elements to the left 
        and throw away the first element
        If we want to rotate we store the first element and 
        Store it to the last index
        '''
        for i in range(self.length):
            self.arr[i] = self.arr[i+1]
    
    def rotate_by_d(self, d):
        """
        call rotate by d times
        time complexity O(n * d) and space complexity O(1).
        """
        if d == 0:
            return 'There is nothing to rotate. \n Exiting !!!'
        for _ in range(d):
            self.LeftShift()
        return self.arr

    def AlgorithmSorted(self):
        '''
        Checking if our arrays is sorted
        '''
        for i in range(self.length-1):
            if self.arr[i+1] < self.arr[i]:
                return False
        return True
        
    def InsertElementInSortedArray(self, ele):
        '''
        Start the index from the end of the array 
        Continue to check if the element at index is greater than 
        Element we want to insert. Shift to the right until condition
        Fails then insert element
        '''
        i = self.length -1 
        while self.arr[i] > ele:
            self.arr[i+1] = self.arr[i]
            i -=1
        self.arr[i+1] = ele
        self.length +=1

    def RearrangeNegativePositive(self):
        '''
        Place all negative integers on the left side
        Place all positive integers on the right side
        '''
        i, j = 0, self.length -1
        while i < j:
            while(self.arr[i] < 0):
                i +=1
            while(self.arr[j] >= 0):
                j -=1
            if i < j:
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
  
    def MergeSortedArrays(arr1, arr2):
        '''
        Copy the smaller elements between array A & array B
        After the while loop copy the remaining elements 
        '''
        m, n = len(arr1), len(arr2)
        i,j = 0,0
        merged_arr = []
        while(i < m and j < n):
            if arr1[i] < arr2[j]:
                merged_arr.append(arr1[i])
                i +=1
            else:
                merged_arr.append(arr2[j])
                j +=1
        for _ in arr1[i:]:
            merged_arr.append(arr1[i])
        for _ in arr2[j:]:
            merged_arr.append(arr2[j])

        return merged_arr



        

       
    
    

        
