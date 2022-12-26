class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        left = 0
        right = 0
        longest_sub = 0
        window = set()
        while right < len(s):
            if s[right] in window:
                window.discard(s[left])
                left += 1
            else:
                window.add(s[right])
                right += 1
            longest_sub = max(longest_sub, right - left)
        return longest_sub