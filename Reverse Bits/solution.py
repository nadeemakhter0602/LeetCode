class Solution:
    def reverseBits(self, n: int) -> int:
        for i in range(16):
            l = (n & 1 << i) << (31 - 2*i)
            r = (n & 1 << (31 - i)) >> (31 - 2*i)
            n &= ~ (1 << i)
            n &= ~ (1 << (31 - i))
            n |= l
            n |= r
        return n
