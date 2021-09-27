"""
Link: https://leetcode.com/problems/reverse-integer/
Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0
"""

class Solution2:
    def reverse(self, x: int) -> int:
        sum = 0
        sign = 1 
        BitInt = 2147483647
        BitNegativeInt = -2147483648
        if x < 0:
            sign = -1
            x = x * sign 
        
        while x > 0:
            pop = x % 10
            
            sum = sum * 10 + pop
            
            x = x // 10
            
        if not BitNegativeInt < sum < BitInt:
            return 0
        
        sum = sign*sum
        
        return sum
