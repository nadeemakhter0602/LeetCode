class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        position = dict()
        for i in range(len(nums)):
            if nums[i] in position:
                if abs(i - position[nums[i]]) <= k:
                    return True
            position[nums[i]] = i
        return False
