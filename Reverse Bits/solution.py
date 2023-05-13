class Solution:
    def reverseBits(self, n: int) -> int:
        r = 0
        for i in range(31):
            r |= (n & 1 << i) > 0
            r <<= 1
        r |= (n & 1 << 31) > 0
        return r
