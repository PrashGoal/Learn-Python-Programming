"""
Link: https://leetcode.com/problems/valid-parentheses/
Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true
"""

class Solution5:
    def isValid(self, s: str) -> bool:
        stack = []
        
        closeToopen = {')':'(', ']':'[', '}':'{'}
        
        for c in s:
            if c in closeToopen:
                if stack and stack[-1] == closeToopen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
