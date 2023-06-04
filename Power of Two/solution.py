import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n >= 1 and 2 ** int(math.log2(n)) == n
