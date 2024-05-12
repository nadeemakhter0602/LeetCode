class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        maxLocal = []
        for i in range(1, len(grid) - 1):
            row = []
            for j in range(1, len(grid) - 1):
                max_center = float("-inf")
                max_center = max(
                    [
                        grid[i][j],
                        grid[i - 1][j - 1],
                        grid[i + 1][j + 1],
                        grid[i][j + 1],
                        grid[i + 1][j],
                        grid[i - 1][j],
                        grid[i][j - 1],
                        grid[i + 1][j - 1],
                        grid[i - 1][j + 1],
                    ]
                )
                row.append(max_center)
            maxLocal.append(row)
        return maxLocal
