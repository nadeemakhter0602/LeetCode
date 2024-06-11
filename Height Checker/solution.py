class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        max_height = max(heights) + 1
        expected = [0 for i in range(max_height)]
        for i in heights:
            expected[i] += 1
        idx = 0
        n = 0
        for i in range(1, max_height):
            if expected[i] == 0:
                continue
            while expected[i] > 0:
                if heights[idx] != i:
                    n += 1
                expected[i] -= 1
                idx += 1
        return n
