import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n >= 1 and math.pow(2, int(math.log(n, 2))) == n
