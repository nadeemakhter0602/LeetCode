class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        n = len(nums)
        for i in range(n):
            if i + 1 < n and nums[i] != nums[i+1]:
                nums[k - 1] = nums[i]
                k += 1
        if nums[k - 2] != nums[-1]:
            nums[k - 1] = nums[-1]
        return k
