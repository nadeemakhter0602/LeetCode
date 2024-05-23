class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(idx, subset, powerset):
            if idx >= len(nums):
                powerset.append(subset)
                return powerset
            dfs(idx + 1, subset, powerset)
            dfs(idx + 1, subset + [nums[idx]], powerset)
            return powerset

        powerset = dfs(0, [], [])
        return powerset
