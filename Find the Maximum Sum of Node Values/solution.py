class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        changes = []
        maxValue = 0
        for num in nums:
            maxValue += num
            changes.append((num ^ k) - num)
        changes.sort(reverse=True)
        for i in range(0, len(changes) - 1, 2):
            change1 = changes[i]
            change2 = changes[i + 1]
            if change1 + change2 > 0:
                maxValue += change1 + change2
        return maxValue
