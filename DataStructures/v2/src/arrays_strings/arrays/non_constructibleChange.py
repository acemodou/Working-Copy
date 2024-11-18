from typing import List 

def simple_assert(a, b):
    assert a == b, f'{a}!{b}'
    
def nonConstructibleChange(coins : List[int]):
    # Write your code here.
    change = 0
    coins.sort()
    for coin in coins:
        if change + 1 < coin:
            return change + 1
        change += coin
    return change + 1
    


input = [5, 7, 1, 1, 2, 3, 22]
expected = 20
actual = nonConstructibleChange(input)
simple_assert(actual, expected)
