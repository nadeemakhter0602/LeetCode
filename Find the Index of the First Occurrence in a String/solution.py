class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l1 = 0
        n = len(needle)
        h = len(haystack)
        while l1 < h:
            b = l1
            l2 = 0
            while l1 < h and l2 < n and haystack[l1] == needle[l2]:
                l2 += 1
                l1 += 1
            if l2 == n:
                return l1 - l2
            l1 = b
            l1 += 1
        return -1
