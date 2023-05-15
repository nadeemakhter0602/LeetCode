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


'''
# Creating lookup table for O(1) time complexity
class Solution:
    def __init__(self):
        self.lookup = []
        for j in range(65536):
            n = j
            for i in range(16):
                l = (n & 1 << i) << (31 - 2 * i)
                r = (n & 1 << (31 - i)) >> (31 - 2 * i)
                n &= ~ (1 << i)
                n &= ~ (1 << (31 - i))
                n |= l
                n |= r
            self.lookup.append(n)

    def reverseBits(self, n: int) -> int:
        return self.lookup[n >> 16] >> 16 | self.lookup[n & 0xffff]

'''
