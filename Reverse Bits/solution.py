class Solution:
    def reverseBits(self, n: int) -> int:
        r = 0
        for i in range(31):
            lsb = n & 1
            r |= lsb
            r = r << 1
            n = n >> 1
        lsb = n & 1
        r |= lsb
        return r
