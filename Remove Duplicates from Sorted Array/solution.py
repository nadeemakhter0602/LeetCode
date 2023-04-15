class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        n = len(nums)
        for i in range(n):
            if i + 1 < n and nums[i] != nums[i + 1]:
                nums[k] = nums[i]
                k += 1
        if k > 0 and nums[k - 1] != nums[n - 1]:
            nums[k] = nums[n - 1]
            k += 1
        elif k == 0:
            k = 1
        return k
