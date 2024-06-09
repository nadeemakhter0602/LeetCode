class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        s, n = 0, 0
        prefix = [0 for i in range(k)]
        prefix[0] = 1
        for i in range(len(nums)):
            s += nums[i]
            rem = s % k
            n += prefix[rem]
            prefix[rem] += 1
        return n
