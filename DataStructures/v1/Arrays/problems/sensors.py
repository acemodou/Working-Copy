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
    1. Make an iterative approach 
    2. Create a dispatcher function, setup a base case
    3. call the iterative module in the dispatcher
    4. convert iterative module to call the dispatcher.
    '''
    if size == 0: return 0
    lastElementDiff = abs(senosorA[size -1] - senosorB[size -1])
    diff = totalDiffDispatcher(senosorA, senosorB, size -1) + lastElementDiff
    return diff 


if __name__ == "__main__":
    senosorA = [15, -4, 56, 10, -23]
    senosorB = [14, -9 , 56, 14, -23]
    print(F'The total difference in sensor reading is : {totalDiffDispatcher(senosorA, senosorB, 5)}')


