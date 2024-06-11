class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum([i != j for i, j in zip(sorted(heights), heights)])
