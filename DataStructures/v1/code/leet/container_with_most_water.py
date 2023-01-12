from typing import List 
def maxArea(height: List[int]) -> int:
    '''
    Area of a rectangle. Length * width
    Length is the x axis :
    Width is the height. In our case minimum height to avoid 
    water overflowing 
    '''
    max_area = 0
    for x in range(len(height)):
        for y in range(x+1, len(height)):
            length = y - x
            width = min(height[x], height[y])
            max_area = max((length * width), max_area)
    return max_area 

    


for input, expected in [([1,8,6,2,5,4,8,3,7],49),([1,1], 1),
([4,3,2,1,4],16),([1,2,1],2)]:
    output = maxArea(input)
    assert output == expected, f'{output} != {expected}'
