class solution:
    memo  = {}
    def climbStairs(self, n):
        '''
        You are climbing a staircase. It takes n steps to reach the top.
        Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
        Example 1:
            Input: n = 2
            Output: 2
            Explanation: There are two ways to climb to the top.
            1. 1 step + 1 step
            2. 2 steps

        Example 2:
            Input: n = 3
            Output: 3
            Explanation: There are three ways to climb to the top.
            1. 1 step + 1 step + 1 step
            2. 1 step + 2 steps
            3. 2 steps + 1 step
        '''
        if n in self.memo:
            return self.memo[n]
        elif n < 0:
            return 0
        elif n == 0 or n == 1:
            return 1
        else:
            value = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.memo[n] = value
        return value 
    
    def allStairs(self, n, num_steps):
        '''
        Climbing for specific steps 
        '''
        if n < 0:
            return 0
        elif n == 0:
            return 1
        else:
            self.total = 0
            for i in num_steps:
                if (n - i) >= 0:
                    self.total += self.allStairs(n-i, num_steps)
        return self.total

        

# Test cases 
cases = (
    (0,1),
    (1,1),
    (2,2),
    (3,3),
    (4,5),
    )

allcases = (
    (0,1),
    (1,1),
    (3,2),
    (5,5),
    (6,8),
    )

import unittest 
class TestClimbStairs(unittest.TestCase):
    
    def test_climbStairs(self):
        sol = solution()
        for input, expected in cases:
            self.assertEqual(expected, sol.climbStairs(input), 'Did not match: %d' % input)
    
    def test_allStairs(self):
        sol = solution()
        for input, expected in allcases:
            self.assertEqual(expected, sol.allStairs(input, [1,3,5]), 'Did not match: %d' % input)


if __name__ == '__main__':
    unittest.main()
