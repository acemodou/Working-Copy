def totalDiff(senosorA, senosorB):
    '''
    Iterative approach 
    '''

    diff = 0

    for i in range(len(senosorA)):
        diff += abs(senosorA[i] - senosorB[i])
    
    return diff


def totalDiffDispatcher(senosorA, senosorB):
    '''
    Recursive approach
    '''
    size = len(senosorA)

    if size == 0:
        return 0
    lastElementDiff = abs(senosorA[-1] - senosorB[-1])
    
    
    diff = totalDiffDispatcher(senosorA, senosorB) + lastElementDiff
    return diff 
    



if __name__ == "__main__":
    senosorA = [15, -4, 56, 10, -23]
    senosorB = [14, -9 , 56, 14, -23]
    print(F'The total difference in sensor reading is : {totalDiffDispatcher(senosorA, senosorB)}')


