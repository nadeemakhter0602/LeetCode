class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        z = x
        prev = x
        while True:
            z -= (z*z - x) / (2*z)
            if int(prev) == int(z):
                return int(z)
            prev = z
