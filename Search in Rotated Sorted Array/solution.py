class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # check if we are in first half of array
            if nums[mid] >= nums[left]:
                if nums[mid] < target:
                    left = mid + 1
                elif target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            # if we are in second half of array
            else:
                if target < nums[mid]:
                    right = mid - 1
                elif nums[right] < target:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1