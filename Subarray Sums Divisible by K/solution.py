class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        s = 0
        prefix = dict()
        n = 0
        for i in range(len(nums)):
            s += nums[i]
            rem = s % k
            if rem == 0:
                n += 1
            if rem in prefix:
                n += prefix[rem]
            prefix[rem] = 1 + prefix.get(rem, 0)
        return n
