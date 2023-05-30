class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        z = x
        for i in range(20):
            z -= (z*z - x) / (2*z)
        return int(z)
