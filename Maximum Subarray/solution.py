class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        maxsum = nums[0]
        for i in nums:
            s += i
            if s > maxsum:
                maxsum = s
            if s < 0:
                s = 0
        return maxsum