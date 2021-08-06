import unittest
from parameterized import parameterized
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Time is O(n^2), O(1) space
        '''
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j] 
        return []
    
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        '''
         Time is O(n^2), O(1) space
         '''
        cache = {}
        for key, value in enumerate(nums):
            if value in cache:
                return [cache[value], key]
            cache[target - value] = key
        return []
            

class TestTwoSum(unittest.TestCase):
    @parameterized.expand([
         ([2,7,11,15], 9, [0, 1]),
        ([3,2,4], 6, [1,2]),
        ([3,3], 6, [0,1])
    ])

    # def test_twoSum(self, input: List[int], target: int, expected: List[int]) -> List[int]:
    #     sol = Solution()
    #     self.assertEqual(expected, sol.twoSum(input, target))
    
    def test_twoSum(self, input: List[int], target: int, expected: List[int]) -> List[int]:
        sol = Solution()
        self.assertEqual(expected, sol.two_sum(input, target))

if __name__ == '__main__':
    unittest.main()