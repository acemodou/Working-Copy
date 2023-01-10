import unittest
from parameterized import parameterized

class solution:
    '''
    mod = n - math.floor(n/base) * base

    '''
    def reverse(self, x: int) -> int:
        def mod(number: int, m: int) -> int:
            if number < 0:
                return number % -m 
            else:
                return number % m
    
        def divide(number, divisor) -> int:
            return int(number * 1.0 / divisor)
    
        rev: int = 0
        MAX_INT = (2 ** 31) - 1 
        MIN_INT = -2 ** 31
        # while x:
        #     last_digit = mod(x, 10)
        #     x = divide(x, 10)
        #     if rev > divide(MAX_INT,10) or (rev == divide(MAX_INT, 10) and last_digit > 7):
        #         return 0
        #     if rev < divide(MIN_INT,10) or (rev == divide(MIN_INT, 10) and  last_digit < -8):
        #         return 0
        #     rev = rev * 10 + last_digit
        # return rev 
        negative = x < 0 
        x = abs(x)
        while x:
            last_digit =  x % 10
            x = x // 10
            rev = rev * 10 + last_digit
        if negative:
            rev = -rev 
        if rev > MAX_INT or rev < MIN_INT:
            return 0
        return rev 

class TestReverse(unittest.TestCase):
    @parameterized.expand([
         ('123', 123, 321),
        ('-123', -123, -321),
        ('120', 120, 21),
        ('0', 0, 0),
        ('num',1534236469,0),
        ('bignum',1463847412,2147483641)
    ])
    
    def test_reverse(self, _, input, expected):
        sol = solution()
        self.assertEqual(expected, sol.reverse(input))

if __name__ == '__main__':
    unittest.main()


    '''
    121 
    degree = 2
    1 **(1) // 10 ** (2)
    '''