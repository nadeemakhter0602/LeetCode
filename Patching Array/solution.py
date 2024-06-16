class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        missing = 1
        patches = 0
        idx = 0
        while missing <= n:
            if idx < len(nums) and nums[idx] <= missing:
                missing += nums[idx]
                idx += 1
            else:
                missing += missing
                patches += 1
        return patches
