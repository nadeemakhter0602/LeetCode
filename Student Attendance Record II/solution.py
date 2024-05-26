class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        memo = [[[-1 for k in range(2)] for j in range(3)] for i in range(n)]

        def recurse(i, absents, lates):
            if absents > 1 or lates > 2:
                return 0
            if i == n:
                return 1
            if memo[i][lates][absents] != -1:
                return memo[i][lates][absents]
            count = recurse(i + 1, absents + 1, 0)
            count += recurse(i + 1, absents, lates + 1)
            count += recurse(i + 1, absents, 0)
            memo[i][lates][absents] = count % MOD
            return count

        return recurse(0, 0, 0) % MOD
