"""
Link: https://leetcode.com/problems/longest-common-prefix/
Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""
class Solution6:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res = res+strs[0][i]
        return res

