def simple_assert(a:int, b:int):
    assert a == b, f'{a}!{b}'


def nonConstructibleChange(coins):
    # Write your code here.
    coins.sort()
    change = 0
    for i in range(len(coins)):
        if change + 1 < coins[i]:
            return change + 1
        change += coins[i]
        
    
simple_assert(nonConstructibleChange([5, 7, 1, 1, 2, 3, 22]), 20)
simple_assert(nonConstructibleChange([1, 2, 5]), 4)
simple_assert(nonConstructibleChange([7]), 1)
