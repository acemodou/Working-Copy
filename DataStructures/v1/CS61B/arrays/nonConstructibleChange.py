from simpleAssert import simple_assert
from typing import List

# O(nlog(n)) time | O(1) space 
def nonConstructibleChange(coins : List[int]) -> int:
    change = 0
    coins.sort()

    for coin in coins:
        if coin > change + 1:
            return change + 1
        change += coin
    return change + 1
        


simple_assert(nonConstructibleChange([5, 7, 1, 1, 2, 3, 22]), 20)
simple_assert(nonConstructibleChange([1, 1, 1, 1, 1]), 6)






