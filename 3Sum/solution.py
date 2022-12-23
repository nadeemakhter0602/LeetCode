class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            target = -nums[i]
            while l < r:
                val = nums[l] + nums[r]
                if val == target:
                    while l < r and nums[l] == nums[l+1]:
                        l+=1
                    triplets.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1
                elif val < target:
                    l+=1
                else:
                    r-=1
        return triplets