class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        maxSum = 0
        isOdd = 0
        minChange = float("inf")
        for num in nums:
            change = (num ^ k) - num
            minChange = min(abs(change), minChange)
            if change > 0:
                isOdd ^= 1
                maxSum += num + change
            else:
                maxSum += num
        if isOdd:
            maxSum -= minChange
        return maxSum
