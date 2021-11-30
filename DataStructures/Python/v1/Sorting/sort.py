
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
        for i in range(1, self.size):
            x = self._arr[i]
            j = i - 1 
            while(j > -1 and self._arr[j] > x):
                self._arr[j+1] = self._arr[j]
                j -= 1
            self._arr[j+1] = x 
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
            temp = A[x]
            A[x] = A[y]
            A[y] = temp 

    def partion(self, A, start, end):
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
            j = self.partion(A, low, high)
            self.quick_sort(A, low, j)
            self.quick_sort(A, j+1, high) 
        return A 