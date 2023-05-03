class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = dict()
        l = 0
        o = 0
        for i in s:
            count[i] = 1 + count.get(i, 0)
        for i in count:
            m = count[i] % 2
            l += count[i] - m
            if m == 1:
                o = 1
        return l + o
