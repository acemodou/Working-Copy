
class Sorting:
    _arr = []
    size = 0
    def __init__(self, A, N):
        self._arr = A
        self.size = N 

        ''' Initialize the array  '''
        self._arr = [0] * N
    
    def bubble_sort(self, A):
        self._arr = A
        for i in range(self.size-1):
            for j in range(self.size-i-1):
                if self._arr[j] > self._arr[j+1]:
                    self._arr[j], self._arr[j+1] = self._arr[j+1], self._arr[j]
        return self._arr
    
    def adaptive_bubble_sort(self, A):
        self._arr = A
        for i in range(self.size-1):
            flag = 0
            for j in range(self.size-i-1):
                if self._arr[j] > self._arr[j+1]:
                    self._arr[j], self._arr[j+1] = self._arr[j+1], self._arr[j]
                    flag = 1
            if flag == 0:
                return True
            
        return False 
    
    def insertion_sort(self, A):
        self._arr = A
        for j in range(1, self.size):
            i = j - 1
            key = self._arr[j]
            while i >= 0 and self._arr[i] > key:
                self._arr[i+1] = self._arr[i]
                i -= 1
            self._arr[i+1] = key
        return self._arr
    
    def selection_sort(self, A):
        self._arr = A 
        for i in range(self.size):
            k = i 
            for j in range(i, self.size):
                if self._arr[j] < self._arr[k]:
                    k = j 
            self._arr[i], self._arr[k] = self._arr[k], self._arr[i]
        return self._arr
    
    def swap(self, A, x, y):
        if x != y:
            A[x], A[y] = A[y], A[x]

    def partition(self, A, start, end):
        pivot_index = start
        pivot = A[pivot_index]

        while start < end:
            while start < len(A) and  A[start] <= pivot:
                start += 1 
            while A[end] > pivot:
                end -= 1
            if start < end:
                self.swap(A, start, end)
        self.swap(A, pivot_index, end)
        return end  

    def quick_sort(self, A, low, high):
        if low < high:
            j = self.partition(A, low, high)
            self.quick_sort(A, low, j-1)
            self.quick_sort(A, j+1, high) 
        return A 
    
    def merge(self, A, low, mid, high):
        i, j, k = low, mid + 1, low
        B = [0] * len(A)

        while i <= mid and j <= high:
            if A[i] < A[j]:
                B[k] = A[i]
                i += 1
                k += 1
            else:
                B[k] = A[j]
                j += 1
                k += 1
    
        for _ in A[i: mid+1]:
            B[k] = A[i]
            i += 1
            k += 1
        
        for _ in A[j: high+1]:
            B[k] = A[j]
            j += 1
            k += 1
        
        for i in range(low, high+1):
            A[i] = B[i]

    def merge_sort(self, A, N):
        win_size = 1
        while win_size <= N:
            win_size *= 2
            i = 0
            while i + win_size -1 <= N:
                low, high = i, i + win_size -1
                mid = (low + high) // 2
                self.merge(A, low, mid, high)
                i = i + win_size

        if (win_size // 2) < len(A):
            self.merge(A, 0, (win_size // 2)-1, N)
        
        return A 
    
    def recursive_merge_sort(self, A, low, high):
        if low < high:
            mid = (low + high) // 2
            self.recursive_merge_sort(A, low, mid)
            self.recursive_merge_sort(A, mid+1, high)
            self.merge(A, low, mid, high)
        return A 
        
    def count_sort(self, A):
        max_element = max(A)
        
        max_element += 1
        count = [0] * max_element
        for i in range(len(A)):
            count[A[i]] += 1

        i , j = 0, 0
        while j < max_element:
            if count[j] > 0:
                A[i] = j
                count[j] -= 1
                i += 1
            else:
                j += 1
        return A 
        
    def shell_sort(self, A):
        gap = len(A)
        while gap > 1:
            gap = gap // 2

            for i in range(gap, len(A)):
                temp = A[i]
                j = i - gap 
                while j >= 0 and A[j] > temp:
                    A[j+gap] = A[j]
                    j = j - gap 
                A[j+gap] = temp
        return A 
    
    class Node:
        def __init__(self, data):
            self.data = data 
            self.next = None 
        
    class singly_list:
        def __init__(self):
            self.head = None
        
        def create(self, ele):
            new_node = Sorting.Node(ele)
            new_node.next = None 
            return new_node
        
        def insert(self, ele):
            if self.head == None:
                self.head = self.create(ele)
                return 
            
            ptr = self.head 
            while ptr.next != None:
                ptr = ptr.next 
            ptr.next = self.create(ele)
        
        def is_empty(self):
            return self.head is None 
        
        def delete_element(self):
            if self.head == None:
                raise NotImplementedError('We should never try to delete and empty Node')
            val = self.head.data
            self.head = self.head.next 
            return val 

    def bucket_sort(self, A):
        max_ele = max(A)
        max_ele += 1
        bins = [self.singly_list() for _ in range(max_ele)]

        for i in range(len(A)):
            bins[A[i]].insert(A[i])
        
        i, j = 0, 0
        while j < max_ele:
            while not bins[j].is_empty():
                A[i] = bins[j].delete_element()
                i += 1
            j += 1
        return A 
    
    def radix_sort(self, A):
        def get_digit_len(n):
            while n > pow(10, i):
                i += 1
            return i + 1

        max_ele = max(A)
        digit_len = get_digit_len(max_ele)

        radix = [self.singly_list() for _ in range(10)]

        for i in range(digit_len):
            for j in range(len(A)):
                radix[A[j] // pow(10, i) % 10].insert(A[j])

            bin_number, array_entry = 0, 0 
            while bin_number < 10:
                while not radix[bin_number].is_empty():
                    A[array_entry] = radix[bin_number].delete_element()
                    array_entry += 1
                bin_number += 1
        return A 
