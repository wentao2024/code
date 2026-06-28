
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/



"""Example 1:
Input: s = "abcabcbb"
Output: 3"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        res = 0
        x = {}
        l = 0
        for r in range(len(s)):
            char = s[r]
            if char in x and x[char]>= l:
                l = x[char]+1
            x[char] = r
            res = max(res, r - l+1)
            
        return res
