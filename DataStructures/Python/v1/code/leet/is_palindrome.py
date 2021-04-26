from parameterized import parameterized
import unittest

class Solution:
    def isPalindrome(self, x):
        x = str(x)
        self.j = len(x) -1 
        self.i = 0
        while self.j >= self.i:
            if x[self.j] != x[self.i]:
                return False
            self.j -= 1
            self.i += 1
        return True
    
    def revInteger(self, num):
        self.rev = 0 
        while num > 0:
            self.get_last_digit = num % 10 
            self.rev = self.rev * 10 + self.get_last_digit
            num //= 10
        return self.rev 

    def is_palindrome2(self, x):
        return self.revInteger(x) == x

class TestLeetCode(unittest.TestCase):
    @parameterized.expand([
         ('121', 121, True),
        ('-121', -121, False),
        ('10', 10, False),
        ('-101', -101, False),
        ('bignum', 3456543, True),
    ])

    # def test_isPalindrome(self):
    #     sol = Solution()
    #     for input, expected in cases:
    #         self.assertEqual(expected, sol.isPalindrome(input))

    # def test_isPalindrome2(self):
    #     sol = Solution()
    #     for input, expected in cases:
    #         self.assertEqual(expected, sol.is_palindrome2(input), 'Did not match: %d' % input)

    # def test_isPalindrome(self, _, input, expected):
    #     sol = Solution()
    #     self.assertEqual(expected, sol.isPalindrome(input))
    
    def test_isPalindrome2(self, _, input, expected):
        sol = Solution()
        self.assertEqual(expected, sol.is_palindrome2(input))

if __name__ == '__main__':
    unittest.main()
   
    

