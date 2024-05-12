class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        maxLocal = []
        for i in range(n - 2):
            row = []
            queue = []
            for j in range(n):
                queue.append(max(grid[i][j], grid[i + 1][j], grid[i + 2][j]))
                if len(queue) >= 3:
                    row.append(max(queue[-1], queue[-2], queue[-3]))
            maxLocal.append(row)
        return maxLocal
