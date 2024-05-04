class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def coin_change(idx, amount, coins, cache=dict()):
            if (amount, idx) in cache:
                return cache[(amount, idx)]
            if amount < 0:
                return 0
            elif amount == 0:
                return 1
            total = 0
            for i in range(idx, len(coins)):
                total += coin_change(i, amount - coins[i], coins, cache)
            cache[(amount, idx)] = total
            return total

        return coin_change(0, amount, coins)
