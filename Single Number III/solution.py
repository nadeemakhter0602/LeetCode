class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_total = 0
        for num in nums:
            xor_total ^= num
        idx_1 = 1
        while not xor_total & idx_1:
            idx_1 <<= 1
        ele1, ele2 = 0, 0
        for num in nums:
            if num & idx_1:
                ele1 ^= num
            else:
                ele2 ^= num
        return [ele1, ele2]
