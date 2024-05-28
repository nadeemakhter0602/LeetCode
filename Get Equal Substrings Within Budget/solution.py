class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        costs = [abs(ord(s[i]) - ord(t[i])) for i in range(n)]
        l = 0
        maxLen = 0
        cost = 0
        for r in range(n):
            cost += costs[r]
            if cost > maxCost:
                cost -= costs[l]
                l += 1
            maxLen = max(r - l + 1, maxLen)
        return maxLen
