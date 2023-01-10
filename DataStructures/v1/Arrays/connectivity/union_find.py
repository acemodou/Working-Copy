import os 
from typing import List 
class QuickFindUF:
   __id = []                # Data Structure to store values 
   __count = 0              # Number of components  

   def __init__(self, N:int) -> None:
       ''' Initialize the array, count and id array'''
       self.__count = N
       self.__id = [0] * N 

       for i in range(N):
           self.__id[i] = i

   def find(self, value:int) -> int:
       ''' return the value id'''
       return self.__id[value]

   def connection(self, p:int, q:int) -> bool:
       return self.find(p) == self.find(q)
    
   def count(self) -> int:
        return self.__count
    
   def idArray(self) -> List[int]:
       print(f'\nDisplaying results: {self.__id}')

   def union(self, p:int, q:int) -> None:
       '''Merge components p and q by setting q as the parent. '''
       pRoot = self.find(p)
       qRoot = self.find(q)

       if pRoot == qRoot: return 
    
       # Setting all occurrences of pRoot id to qRoot 
       for i in range(len(self.__id)):
           if self.__id[i] == pRoot:
               self.__id[i] = qRoot
       self.__count -= 1

if __name__ == '__main__':
    ''' Read the test data '''
    dir_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tinyUF.txt')
    with open(dir_path) as f:
        lines = f.readlines()

    N = int(lines[0])                       # Get the first element in the test data
    QF = QuickFindUF(N)                     # Create a new context of QF

    # Read the pairs which represent connection
    for pairs in lines[1:]:
        p,q = pairs.split( )
        
        # If there is a connection skip
        if QF.connection(int(p), int(q)):
            print(f'Skipping {p} and {q} since they are already connected') 
            continue
        # Established a connection 
        QF.union(int(p), int(q))
        print(f'{p} : {q} are now connected!!!')
    QF.idArray()
    print(f'\nThere were {QF.count()} connected components')
        


    


