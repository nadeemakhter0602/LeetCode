class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        s = 0
        prefix = dict()
        for i in range(len(nums)):
            s += nums[i]
            rem = s % k
            if rem == 0 and i > 0:
                return True
            if rem in prefix:
                if i - prefix[rem] > 1:
                    return True
            else:
                prefix[rem] = i
        return False
