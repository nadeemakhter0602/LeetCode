class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        def checkBeautiful(subset):
            if len(subset) == 0:
                return False
            elif len(subset) == 1:
                return True
            subSet = set(subset)
            for element in subset:
                if element + k in subSet:
                    return False
            return True

        def dfs(i, subset, powerset):
            if i >= len(nums):
                if checkBeautiful(subset):
                    powerset.append(subset)
                return subset
            dfs(i + 1, subset, powerset)
            dfs(i + 1, subset + [nums[i]], powerset)
            return subset

        powerset = []
        dfs(0, [], powerset)
        return len(powerset)
