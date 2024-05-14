class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rowLen = len(grid)
        columnLen = len(grid[0])

        def dfs(r, c, grid, visited):
            if (
                r == rowLen
                or c == columnLen
                or r < 0
                or c < 0
                or grid[r][c] == 0
                or (r, c) in visited
            ):
                return 0
            visited.add((r, c))
            maxGold = float("-inf")
            maxGold = max(maxGold, grid[r][c] + dfs(r - 1, c, grid, visited))
            maxGold = max(maxGold, grid[r][c] + dfs(r + 1, c, grid, visited))
            maxGold = max(maxGold, grid[r][c] + dfs(r, c - 1, grid, visited))
            maxGold = max(maxGold, grid[r][c] + dfs(r, c + 1, grid, visited))
            visited.discard((r, c))
            return maxGold

        maximumGold = 0
        for r in range(rowLen):
            for c in range(columnLen):
                maximumGold = max(maximumGold, dfs(r, c, grid, set()))
        return maximumGold
