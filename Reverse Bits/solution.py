class Solution:
    def reverseBits(self, n: int) -> int:
        r = 0
        for i in range(16):
            r |= (n & 1 << i) << (31 - 2*i)
            r |= (n & 1 << (31 - i)) >> (31 - 2*i)
        return r
