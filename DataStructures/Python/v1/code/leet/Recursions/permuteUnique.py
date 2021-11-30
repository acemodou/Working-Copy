from typing import List
from typing import Set
def permute_unique(strings: List[str]) -> Set[tuple]:
    ans = set()
    n = len(strings)
    
    def back_track(start: int) -> None:
        if start == n:
            ans.add(tuple(strings))
        
        for i in range(start, n):
            strings[start], strings[i] = strings[i], strings[start]
            back_track(start + 1)
            strings[start], strings[i] = strings[i], strings[start]

    back_track(0)
    return ans

def set_of_tuples_to_list(strings: List[str]) -> List[List[int]]:
    set_of_tuples = permute_unique(strings)
    res = [list(ele) for ele in set_of_tuples]
    return res


def permute(strings: List[str]) -> List[List[int]]:
    result = []
    n = len(strings)

    def back_track(start: int) -> None:
        if start == n:
            result.append(strings.copy())
        
        for i in range(start, n):
            strings[start], strings[i] = strings[i], strings[start]
            back_track(start + 1)
            strings[start], strings[i] = strings[i], strings[start]

    back_track(0)
    unique = []
    [unique.append(n) for n in result if n not in unique] # Removes dup 
    return unique  


