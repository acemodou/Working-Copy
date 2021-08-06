'''
1.Design: Read in number of objects N from standard input 
2. Repeat:
    2.a Read in pair of integers from standard input 
    2.b If they are not yet connected, connect them and print out the pair

'''
class QuickFindUF:
    __id =[]
    
    def __init__(self, N):
        ''' Set IDS of each object to itself '''
        self.__id = [0] * N 
        for id in range(N):
            self.__id[id] = id 
        print(self.__id)
    
    def connected(self, p, q) -> bool:
        ''' Return true if the Ids are connected '''
        return self.__id[p] == self.__id[q]
    
    def union(self, p, q):
        pid = self.__id[p]
        qid = self.__id[q]
        for i in range(len(self.__id)):
            if self.__id[i] == pid:
                self.__id[i] = qid
        print(self.__id)

if __name__ == '__main__':
    N = int(input('How many values to enter: '))
    UF = QuickFindUF(N)
    for i in range(N):
        p = int(input("Enter p: "))
        q = int(input("Enter q: "))
        if UF.connected(p, q):
            continue
        UF.union(p,q)
        print(f'{p} and  {q} are now connected')
    


