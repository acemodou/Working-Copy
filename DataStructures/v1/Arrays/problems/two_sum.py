from typing import List

def simple_assert(a:int, b:int):
    assert a == b, f'{a}!{b}'


def two_sum(nums: List[int], target: int) -> List[int]:
    if len(nums) < 2:
        return []

    seen = {}
    for key, value in enumerate(nums):
        if (target - value) in seen:
            return [seen[target-value], key]
        seen[value] = key 

def display_two_pairs(nums: List[int], target: int) -> List[int]:
    
    max_count = max(nums)
    hash_table = [0 for _ in range(max_count+1)]

    for i in range(len(nums)):
        if hash_table[target - nums[i]] != 0:
            print(f"{[target - nums[i], nums[i]]} = {target}")
        hash_table[nums[i]] += 1

def twoNumberSum(array: List[int], targetSum: int) -> List[int]:
    if len(array) < 2:
        return []

    seen = {}
    for key, value in enumerate(array):
        if (targetSum - value) in seen:
            return [targetSum-value, value]
        seen[value] = key

    return []


nums = [3, 3]
simple_assert(two_sum(nums, target=6), [0, 1])

nums = [3, 5, -4, 8, 11, 1, -1, 6]
simple_assert(twoNumberSum(nums, targetSum=10), [11, -1])

nums = [6,3,8,10,16,7,5,2,9,14]
display_two_pairs(nums, target=10)



