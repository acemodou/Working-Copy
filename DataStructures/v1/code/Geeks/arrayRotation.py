class Rotation:
    def rotate_left_by_One(self, arr):
        '''
        Rotate the array left by one
        '''
        self.temp = arr[0]
        for values in range(len(arr)-1):
            arr[values] = arr[values+1]
        arr[-1] = self.temp
    
    def rotate_right_by_One(self, arr):
        '''
        Rotate the array right by one
        '''
        self.temp = arr[-1]
        for values in range(len(arr)-1, -1, -1):
            arr[values] = arr[values -1]
        arr[0] = self.temp
    
    def rotate_right(self, arr, k):
        '''
        We use an extra array in which we place every element of the 
        array at its correct position i.e. the number at index i in
        the original array is placed at the index 
       (i+k)% length of array. 
        Then, we copy the new array to the original one.
        '''
        self.aux = len(arr) * [0]
        for i in range(len(arr)):
            self.aux[(i + k) % len(arr)] = arr[i]

        arr[:] = self.aux
        return arr 
        
    def rotate_by_d(self, arr, d):
        '''
        This function called rotate left by one and rotate the array by d
        '''
        for _ in range(d):
            # self.rotate_left_by_One(arr)
            self.rotate_right_by_One(arr)
        print(arr)
        return arr 
    
    def juggling_algorithm(self, A,  k):
        '''
        euclidian_gcd to divide the elements in sets
        Time is O(n) and space is O(1)
        '''
        def euclidian_gcd(n, k):
            if k == 0:
                return n 
            else:
                return euclidian_gcd(k, n % k)
        
        num_sets = euclidian_gcd(len(A), k)
        for i in range(num_sets):
            j = i
            temp = A[i]

            while True:
                d = (j + k) % len(A)
                if d == i:
                    break
                A[j] = A[d]
                j = d
            A[j]= temp
        return A



rotate_left_cases = (
        (1, [2,3,4,5,6,7,1]),
        (2, [3,4,5,6,7,1,2]),
        (3, [4,5,6,7,1,2,3]),
)

rotate_right_cases = (
        (1, [7,1,2,3,4,5,6]),
        (2, [6,7,1,2,3,4,5]),
        (3, [5,6,7,1,2,3,4]),
)


import unittest 

class TestRotation(unittest.TestCase):

    # def test_rotate_left_by_d(self):
    #     sol = Rotation()
    #     for input, expected in rotate_left_cases:
    #         self.assertEqual(expected, sol.rotate_by_d([1,2,3,4,5,6,7], input), 'Did not match: %d' % input)
           
    def test_juggling_algorithm(self):
        sol = Rotation()
        for input, expected in rotate_left_cases:
            self.assertEqual(expected, sol.juggling_algorithm([1,2,3,4,5,6,7], input), 'Did not match: %d' % input)

    def test_rotate_right_by_d(self):
        sol = Rotation()
        for input, expected in rotate_right_cases:
            self.assertEqual(expected, sol.rotate_right([1,2,3,4,5,6,7], input), 'Did not match: %d' % input)


if __name__ == '__main__':
    unittest.main()