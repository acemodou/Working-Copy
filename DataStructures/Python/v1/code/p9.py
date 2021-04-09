class Solution:
    def isPalindrome(self, x):
        x = str(x)
        self.j = len(x) -1 
        self.i = 0
        while(self.j >= self.i):
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
        if self.revInteger(x) != x:
            return False
        return True 


#Defining test cases here 
cases = (
        (121, True),
        (-121, False),
        (10, False),
        (-101, False),
        (3456543, True),
    )  

import unittest
class TestLeetCode(unittest.TestCase):

    def test_isPalindrome(self):
        sol = Solution()
        for input, expected in cases:
            self.assertEqual(expected, sol.isPalindrome(input))

    def test_isPalindrome2(self):
        sol = Solution()
        for input, expected in cases:
            self.assertEqual(expected, sol.is_palindrome2(input), 'Did not match: %d' % input)

if __name__ == '__main__':
    unittest.main()
   
    

