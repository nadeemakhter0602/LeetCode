class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        count = [0 for i in range(n + 1)]
        for num in nums:
            if num >= n:
                count[n] += 1
            else:
                count[num] += 1
        counter = 0
        for x in range(n, -1, -1):
            counter += count[x]
            if counter == x:
                return x
        return -1
