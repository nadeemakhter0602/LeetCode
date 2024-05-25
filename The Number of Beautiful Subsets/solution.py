class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        def dfs(i, subset, count):
            if i == len(nums):
                return 1
            count = dfs(i + 1, subset, count)
            if subset.get(nums[i] + k, 0) == 0 and subset.get(nums[i] - k, 0) == 0:
                subset[nums[i]] = 1 + subset.get(nums[i], 0)
                count += dfs(i + 1, subset, count)
                subset[nums[i]] -= 1
            return count

        return dfs(0, dict(), 0) - 1
