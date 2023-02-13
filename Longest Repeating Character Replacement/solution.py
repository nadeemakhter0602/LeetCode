class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        right = 0
        maxf = 0
        count = dict()
        longest = 0
        while right < len(s):
            count[s[right]] = 1 + count.get(s[right], 0)
            maxf = max(maxf, count[s[right]])
            if longest < k + maxf:
                longest += 1
            else:
                count[s[right - longest]] -= 1
            right += 1
        return longest