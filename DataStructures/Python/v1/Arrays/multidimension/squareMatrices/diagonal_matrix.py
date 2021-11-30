
class AdvanceMatrix:
    '''
    Understand lower Triangular Matrix 
    '''
    __diagonal = []
    __lowerTriangle = []
    __N = 0

    def __init__(self, N) -> None:
        self.__diagonal = [0] * N 
        self.__lowerTriangle = [0] * (N * (N + 1) // 2)
        self.__N = N 

    def setDiagonal(self, row, col, value) -> None:
        if row == col:
            self.__diagonal[row] = value
    
    def setLowerTriange(self, row, col, value) -> None:
        if row >= col: 
            self.__lowerTriangle[(row * (row-1) // 2) + col -1]  = value

    def getLowerTriangle(self, row, col):
        if row >= col:
            print(self.__lowerTriangle[(row * (row - 1) //2) + col -1], end=' ')
            return self.__lowerTriangle[(row * (row -1) //2) + col -1]

    def getDiagonal(self, row, col):
        if row == col:
            print(self.__diagonal[row], end=' ')
            return self.__diagonal[row]

    def displayDiagonal(self):
        for row in range (len(self.__diagonal)):
            for col in range(len(self.__diagonal)):
                if row == col:
                    self.getDiagonal(row, col)
                else:
                    print("0", end=' ')
            print()
        print()
    
    def displayLowerTriange(self):
        for row in range(1, self.__N+1):
            for col in range(1, self.__N+1):
                if row >= col:
                    self.getLowerTriangle(row, col)
                else:
                    print('0', end=' ')
            print()
        print()

def menu():
    menu_list = {'0': 'Diagonal','1': 'LowerTriangle', '10': 'Exit Application'}
    
    while True:
        for values in sorted(menu_list.keys()):
            print(values, menu_list[values])
        
        selection = input('Choose your selection: ')
        if selection == '0':
            result = AdvanceMatrix(4)
            result.setDiagonal(0,0,3)
            result.setDiagonal(1,1,7)
            result.setDiagonal(2,2,4)
            result.setDiagonal(3,3,9)
            result.displayDiagonal()
        
        if selection == '1':
            from sys import stdin
            n = int(input('Enter Dimension in a single row: '))
            result = AdvanceMatrix(n)

            print('Enter all elements: ')
            for i in range(1, n+1):
                for j in range(1, n+1):
                    value  = int(input(f'Enter values  {i}:{j}: '))
                    result.setLowerTriange(i, j, value)

            result.displayLowerTriange()

        elif selection == '10':
            break

        else:
            print('Please enter a valid selection !!!')
menu()