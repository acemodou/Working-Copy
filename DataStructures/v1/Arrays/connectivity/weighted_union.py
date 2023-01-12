import os 

class WeightedQuickUnion:
    __id = []
    __weights = []
    __count = 0

    def __init__(self, N:int) -> None:
        ''' Initialize the array, and count'''
        self.__id = [0] * N 
        self.__weights = [0] * N 
        self.__count = N 

        for i in range(N):
            self.__id[i] = i 
        
        for i in range(N):
            self.__weights[i] = 1

    def count(self):
        return self.__count

    def idArray(self):
        print(self.__id) 

    def root(self, value:int) -> int:
        while value != self.__id[value]:
            self.__id[value] = self.__id[self.__id[value]]
            value = self.__id[value]
        return value  

    def connection(self, p:int, q:int) -> bool:
        return self.root(p) == self.root(q)

    def union(self, p:int, q:int) -> None:
        pRoot = self.root(p)
        qRoot = self.root(q)

        ''' Make smaller root points to larger one '''
        if pRoot == qRoot:return
        if self.__weights[pRoot] < self.__weights[qRoot]:
            self.__id[pRoot] = qRoot
            self.__weights[qRoot] += self.__weights[pRoot]
        else:
            self.__id[qRoot] = pRoot
            self.__weights[pRoot] += self.__weights[qRoot]
        self.__count -=1

if __name__ == '__main__':
    ''' Read the test data from a file '''
    data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tinyUF.txt')
    with open(data_path) as f:
        content = f.readlines()
    
    N = int(content[0])                     # Get the first element in the test data 
    UF = WeightedQuickUnion(N)                      # Create a new context of Quick Union 
    
    ''' Read the pairs which represent the connection skipping the first line '''
    for pairs in content[1:]:
        p, q = pairs.split()
        print(f'{p}:{q}')

        if UF.connection(int(p), int(q)):continue                 # Skip if there is connection 
        UF.union(int(p), int(q))
        print(f'{p} and {q} are now connected!!!')
    UF.idArray()
    print(f'\n There were {UF.count()} connected components')
