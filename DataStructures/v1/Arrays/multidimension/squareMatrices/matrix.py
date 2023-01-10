__about__ = '''
Brief:
    Diagonal matrix: Is a matrix that M[i, j] = 0 if i != j
    
    Usage:
        It gives us important information on independent componenet in a system

Author(s):
    Modou
'''

from typing import List 
class Diagonal:
    def __init__(self, A: List[int]):
        self.diagonal = A

    def write_diagonal_matrix(self, row:int, col:int, value:int):
        ''' Store the non_zero elements in our matrix '''
        if row == col:
            self.diagonal[row][col] = value

    def display_diagonal_matrix(self):
        ''' Displaying diagonal matrix '''
        return self.diagonal

class lower_triangular_matrix(Diagonal):

    def write_lower_triangular_matrix(self, row: int, col: int, value: int):
        ''' Store the  values in the non zero location '''
        if row >= col:
            self.diagonal[row][col] = value
    
    def display_lower_triangular_matrix(self):
        return super().display_diagonal_matrix()

