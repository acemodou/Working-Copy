from typing import List
class Matrix:

    def __init__(self, m, n, init=True) -> None:
        if init:
            self.entries = [[0] * n for _ in range(m)]
        else:
            self.entries = []
        self.m = m 
        self.n = n 

    @classmethod
    def _getListOfList(cls, m, n):
        validate = [m, n]
        assert all(validate)
        print('Fill in the first row and column \n')
        rows = [[int(input('Fill {} rows: column {}: '.format(m, n))) for _ in range(n)] for _ in range(m)]
        print(rows)
        return cls._makeMatrix(rows) 

    def add(self, mat1, mat2):
        ret = Matrix(self.m, self.n)
        for numbers in range(self.m):
            row = [sum(item) for item in zip(mat1[numbers], mat2[numbers])]
            ret[numbers] = row
            print(row)
        return ret 
    
    def subtract(self, mat1, mat2):
        ret = Matrix(self.m, self.n)
        for numbers in range(self.m):
            row = [item[0] - item[1] for item in zip(mat1[numbers], mat2[numbers])]
            ret[numbers] = row
            print(row)
        return ret 
    
    def multiply(self, mat1, mat2):
        ret = Matrix(self.m, self.n)
        for numbers in range(self.m):
            row = [item[0] * item[1] for item in zip(mat1[numbers], mat2[numbers])]
            ret[numbers] = row
            print(row)
        return ret

    def __getitem__(self, idx):
        return self.entries[idx]

    def __setitem__(self, idx, item):
        self.entries[idx] = item

    def transpose(self, mat):
        ''' Transpose the matrix '''

        result = Matrix(self.n, self.m)
        for i in range(self.n):
            for j in range(self.m):
                result[j][i] = mat[i][j]
        print(result[:])

    @classmethod
    def resetMatrix(cls, m, n):
        ''' Reset the matrix data '''
        mat = [[] * n for _ in range(m)]
        print(mat)
        return cls._makeMatrix(mat)
    
    @classmethod
    def makeRandom(cls, m, n, low, high):
        ''' Make a random matrix with elements in range (low, high) '''

        import random
        rows = [[random.randrange(low, high) for _ in range(n)] for _ in range(m)]
        print(rows)
        return cls._makeMatrix(rows)

    @classmethod
    def _makeMatrix(cls, rows):
        ''' Initializing the matrix '''
        m = len(rows)
        n = len(rows[0])
        mat = Matrix(m, n, False)
        mat.entries = rows 
        return mat

    @classmethod
    def fromList(cls):
        rows = cls._getListOfList(2,2)
        return rows
    
    @classmethod
    def makeZeroMatrix(cls, m, n):
        ''' Reset the matrix data '''
        mat = [[0] * n for _ in range(m)]
        print(mat)
        return cls._makeMatrix(mat)

    @classmethod
    def readFromFile(cls, filename):
        ''' Read a matrix from a file  '''
        
        rows = []
        for line in open(filename).readlines():
            row = [int(x) for x in line.split()]
            rows.append(row)
        print(rows)
        return cls._makeMatrix(rows)

    @classmethod
    def saveToFile(cls, filename):
        ''' Save matrix to a file '''
        file = cls.makeRandom(2,2, 1, 9)
        with open(filename, 'w') as f:
            for lines in file:
                f.writelines("%s,\n" % (str(lines)))

def menu():
    ''' Operations to perform '''
    operations = {'0': 'Initialize the matrices','1':'Add two matrices', '2': 'Subtract two matrices', 
        '3': 'Multiply two matrices', '4': 'Transpose two matrices', '5': 'Exit application', 
        '6': 'Reset matrices', '7': 'Make random number matrices', '8': 'Make Zero matrices',
         '9': 'Read matrices from a file', '10': 'Save matrices to a file'}

    while True:
        ''' Sort and print the operations keys '''
        for entries in sorted(operations.keys()):
            print(entries, operations[entries])
        print()
        selection = input('Please choose the operation you want to perform: ')
        if selection == '0':
            print(f'Initializing Matrices : \n')
            result = Matrix(2,2)
            m1 = Matrix.fromList()
            m2 = Matrix.fromList()
            
        elif selection == '1':
            print(f'Adding matrices: \n')
            result.add(m1, m2)
        
        elif selection == '2':
            print(f'Subtracting matrices: \n')
            result.subtract(m1, m2)
        
        elif selection == '3':
            print(f'Multiplying matrices: \n')
            result.multiply(m1, m2)

        elif selection == '4':
            print(f'Transpose matrices: \n')
            result.transpose(m1)

        elif selection == '5':
            import time
            print('Exiting ...')
            time.sleep(2)
            break

        elif selection == '6':
            m1.resetMatrix(2,2)
            m2.resetMatrix(2,2)

        elif selection == '7':
            result = Matrix(2,2)
            m1 = Matrix.makeRandom(2,2, 0, 10)
            m2 = Matrix.makeRandom(2,2, 0, 10)
        
        elif selection == '8':
            m1 = Matrix.makeZeroMatrix(2,2)
            m2 = Matrix.makeZeroMatrix(2,2)

        elif selection == '9':
            import os 
            data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'grid.txt')
            Matrix.readFromFile(data_dir) 
        
        elif selection == '10':
            import os 
            data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'matrix.txt')
            Matrix.saveToFile(data_dir) 

        else:
            print('Please enter a valid choice !!! \n')
menu()


