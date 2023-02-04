class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        target_sum = float('-inf')
        for i in range(n):
            l = i+1
            r = n-1
            while(l<r):
                sums = nums[i]+nums[l]+nums[r]
                if sums==target:
                    return sums
                if abs(target-sums)<abs(target-target_sum):
                    target_sum = sums
                if sums<target:
                    l+=1
                elif sums>target:
                    r-=1
        return target_sum