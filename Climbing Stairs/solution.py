class Solution:
    def climbStairs(self, n: int) -> int:
        n += 1
        sqrt5 = 5 ** 0.5
        Phi = (1 + sqrt5) / 2
        phi = (1 - sqrt5) / 2
        return int((Phi**n - phi**n) // sqrt5)
