class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        subsets = []
        for i in range(1 << N):
            subset = []
            for j in range(N):
                isSet = i >> (N - j - 1) & 1
                if isSet:
                    subset.append(nums[j])
            subsets.append(subset)
        return subsets
