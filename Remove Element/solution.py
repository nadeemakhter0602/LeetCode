class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        r = n - 1
        l = 0
        k = 0
        for i in range(n):
            if nums[i] != val:
                k += 1
        while l < k:
            if nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
            else:
                l += 1
        return k
