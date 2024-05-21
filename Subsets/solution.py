class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(idx, subset, powerset, nums):
            if idx >= len(nums):
                powerset.append(subset)
                return powerset
            dfs(idx + 1, subset, powerset, nums)
            dfs(idx + 1, subset + [nums[idx]], powerset, nums)
            return powerset

        powerset = dfs(0, [], [], nums)
        return powerset
