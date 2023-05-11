class Solution:
    def reverseBits(self, n: int) -> int:
        r = 0
        for i in range(31):
            r = (r | n & 1) << 1
            n = n >> 1
        r |= n & 1
        return r
