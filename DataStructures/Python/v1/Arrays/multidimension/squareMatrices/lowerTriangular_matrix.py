from typing import List 

class LowerTri:
    __lowerTriangle = []
    __N = 0

    def __init__(self, dimension: int) -> None:
        self.__N = dimension
        self.__lowerTriangle = [0] * (self.__N * (self.__N + 1) // 2)
    
    def setLowerTriangle(self, row: int, col: int , value: int) -> None:
        ''' Store values in specific rows '''
        if row >= col:
            self.__lowerTriangle[(row * (row + 1) // 2) + col ] = value 
    
    def getLowerTriangle(self, row: int, col: int) -> List[int]:
        ''' Return the specific value'''
        return self.__lowerTriangle[(row * (row + 1) // 2) + col]
    
    def displayLowerTriangle(self) -> None:
        for i in range(self.__N):
            for j in range(self.__N):
                if i >= j:
                    print(self.getLowerTriangle(i, j), end=' ')
                else:
                    print('0', end=' ')
            print()
        print()


def menu():
    
    menu_list = {'0': 'set lower triangle', '10': 'exit application'}
    
    while True:
        for values in sorted(menu_list.keys()):
            print(f'{values}: {menu_list[values]}')
        
        selection = input('Choose your selection: \n')

        if selection == '0':
            d = int(input('Enter dimension for row major storage: \n'))
            result = LowerTri(d)
            for i in range(d):
                for j in range(d):
                    values = int(input(f'Enter values {i}:{j}: '))
                    result.setLowerTriangle(i, j, values)
            result.displayLowerTriangle()

        elif selection == '10':
            break 

        else:
            print('Enter a valid input!!! \n')


menu()  
