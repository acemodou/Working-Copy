def simple_assert(a, b):
    assert a == b, f'{a}!{b}'

def rectangleMania(coords):
    coords_set = set([(x, y) for x, y in coords])
    rectangle_found = 0
    for x1, y1 in coords:
        for x2, y2 in coords:
            if x2 <= x1 or y2 <= y1:
                continue
            if (x1, y2) in coords_set and (x2, y1) in coords_set:
                rectangle_found += 1 
    
    
    return rectangle_found


coords = [[0, 0], [0, 1], [1, 1], [1, 0], [2, 1], [2, 0], [3, 1], [3, 0]]
simple_assert(rectangleMania(coords), 6)