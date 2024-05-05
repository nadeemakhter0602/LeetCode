class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for i in range(amount + 1)]
        for idx in range(len(coins)):
            for curr_amt in range(amount + 1):
                if curr_amt == 0:
                    dp[curr_amt] = 1
                remaining = curr_amt - coins[len(coins) - 1 - idx]
                if remaining >= 0:
                    dp[curr_amt] += dp[remaining]
        return dp[-1]
