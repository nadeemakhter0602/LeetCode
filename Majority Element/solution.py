class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = dict()
        for i in nums:
            count[i] = 1 + count.get(i, 0)
            if count[i] > len(nums) * 0.5:
                return i
