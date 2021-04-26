class matrix:
    def __init__(self, length):
        self.array = []
        self.length = length
    
    def initialize(self):
        self.array = [0 for _ in range(self.length)]
    
    def setMatrix(self, row, col, element):
        if row == col:
            self.array[row] = element

    def displayDiagonalMatrix(self):
        print(f'Displaying diagonal matrix: {self.array}')
        for row in range(self.length):
            for col in range(self.length):
                if row == col:
                    print(self.array[row], end=' ')
                else:
                    print('0 ', end='')
            print()

diag = matrix(5)
diag.initialize()
diag.setMatrix(0,0,3)
diag.setMatrix(1,1,7)
diag.setMatrix(2,2,4)
diag.setMatrix(3,3,9)
diag.setMatrix(4,4,6)
diag.displayDiagonalMatrix()


# import unittest
# class TestMatrix(unittest.TestCase):
#     def test_diagonal(self):
#         sol = matrix()
#         expected = [[3,0,0,0,0],
#                     [0,7,0,0,0],
#                     [3,0,4,0,0],
#                     [3,0,0,9,0],
#                     [3,0,0,0,6]]
#         result = diag.displayDiagonalMatrix()
#         self.assertEqual(expected, result)



# if __name__ == '__main__':
#     unittest.main()