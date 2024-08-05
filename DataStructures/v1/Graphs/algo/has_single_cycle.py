def simple_assert(a, b):
    assert a == b, f"{a}!{b}"

STARTING_IDX = 0 
    
def hasSingleCycle(array):
    # Write your code here.
    numElementVisited = 0
    currend_idx = STARTING_IDX
    
    while numElementVisited < len(array):
        if numElementVisited > 0 and currend_idx == 0:
            return False 
        numElementVisited += 1
        currend_idx = getNextElement(currend_idx, array)
    return currend_idx == STARTING_IDX

def  getNextElement(currend_idx, array):
    jump = array[currend_idx]
    nextIdx = (currend_idx + jump) % len(array)
    return nextIdx if nextIdx >=0 else nextIdx + len(array)



simple_assert(hasSingleCycle([2, 3, 1, -4, -4, 2]), True)