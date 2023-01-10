def totalDiff(senosorA, senosorB, size):
    '''
    Iterative approach 
    '''
    diff = 0
    for i in range(size):
        diff += abs(senosorA[i] - senosorB[i])
    
    return diff

def totalDiffDispatcher(senosorA, senosorB, size):
    '''
    Convert iterative approach to recursive
    '''
    if size == 0: return 0
    lastElementDiff = abs(senosorA[size -1] - senosorB[size -1])
    diff = totalDiffDispatcher(senosorA, senosorB, size -1) + lastElementDiff
    return diff 


if __name__ == "__main__":
    senosorA = [15, -4, 56, 10, -23]
    senosorB = [14, -9 , 56, 14, -23]
    print(F'The total difference in sensor reading is : {totalDiffDispatcher(senosorA, senosorB, 5)}')


