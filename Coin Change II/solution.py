class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0 for i in range(len(coins))] for i in range(amount + 1)]
        for curr_amt in range(amount + 1):
            for idx in range(len(coins)):
                if curr_amt == 0:
                    dp[curr_amt][idx] = 1
                    continue
                remaining = curr_amt - coins[len(coins) - 1 - idx]
                if remaining >= 0:
                    dp[curr_amt][idx] += dp[remaining][idx]
                dp[curr_amt][idx] += dp[curr_amt][idx - 1] if idx - 1 >= 0 else 0
        return dp[-1][-1]
