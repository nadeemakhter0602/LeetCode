class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        # if array is not rotated
        if nums[left] < nums[right]:
            return nums[left]
        elif right == 0:
            return nums[right]
        # if array is rotated
        while left <= right:
            mid = (left + right) // 2
            if nums[mid + 1] < nums[mid]:
                return nums[mid + 1]
            # if we are in first half of sorted array
            elif nums[left] <= nums[mid]:
                # search right side
                left = mid + 1
            # if we are in second half of sorted array
            else:
                # search left side
                right = mid - 1