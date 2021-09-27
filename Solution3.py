"""
Link: 
Example 1:

Input: x = 121
Output: true
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Example 4:

Input: x = -101
Output: false
"""

class Solution3:
    def isPalindrome(self, x: int) -> bool:
        sum = 0
        temp = x
        
        while x > 0:
            pop = x % 10
            
            sum = sum * 10 + pop
            
            x = x // 10
        
        if sum == temp:
            return True
        else:
            return False
