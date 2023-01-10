
from typing import List 
class Box:
    def __init__(self, height:int, width:int, depth: int) -> None:
        self.h = height
        self.w = width 
        self.d = depth 
    
    def __lt__(self, other):
        ''' This overrides less than to sort base area '''
        return self.w * self.d < other.w * other.d
    
def max_stack_height(arr:List[tuple], n: int):
    '''
    Create a rotation for exam
    '''
    rot = [Box(0, 0, 0) for _ in range(3 * n )]
    idx = 0

    for i in range(n):
        
        # Copy the original box
        rot[idx].h = arr[i].h
        rot[idx].w = min(arr[i].w, arr[i].d)
        rot[idx].d = max(arr[i].w, arr[i].d)
        idx += 1 

        # First rotation of the box 
        rot[idx].h = arr[i].w 
        rot[idx].w = min(arr[i].h, arr[i].d)
        rot[idx].d = max(arr[i].h, arr[i].d)
        idx += 1

        # Second rotation of the box
        rot[idx].h = arr[i].d 
        rot[idx].w = min(arr[i].h, arr[i].w)
        rot[idx].d = max(arr[i].h, arr[i].w)
        idx += 1 
    
    # n increase by 3 
    n *= 3
    
    # # Sort in descending area 
    rot.sort(reverse=True)
    print('Displaying our boxes ... ')
    for i in range(n):
        print(rot[i].h, 'x', rot[i].w, 'x', rot[i].d)
    
    # Get the max stack height 
    msh = [0] * n 
    for i in range(n):
        msh[i] = rot[i].h
    
    # Store the max stack element 
    for i in range(1, n):
        for j in range(0, i):
            if rot[i].w < rot[j].w and rot[i].d < rot[j].d:
                if msh[i] < msh[j] + rot[i].h:
                    msh[i] = msh[j] + rot[i].h

    # Get the max element 
    mst_element = -1
    for i in range(len(msh)):
        mst_element = max(msh[i], mst_element)
    
    return mst_element


if __name__=="__main__":
    arr = [Box(1, 2, 4), Box(3, 2, 5)]
    print(f'Maximum stack height: {max_stack_height(arr, len(arr))}')