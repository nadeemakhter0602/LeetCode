class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rowLen = len(grid)
        columnLen = len(grid[0])

        def dfs(r, c, grid):
            if r == rowLen or c == columnLen or r < 0 or c < 0 or grid[r][c] == 0:
                return 0
            gold = grid[r][c]
            grid[r][c] = 0
            maxGold = float("-inf")
            maxGold = max(maxGold, gold + dfs(r - 1, c, grid))
            maxGold = max(maxGold, gold + dfs(r + 1, c, grid))
            maxGold = max(maxGold, gold + dfs(r, c - 1, grid))
            maxGold = max(maxGold, gold + dfs(r, c + 1, grid))
            grid[r][c] = gold
            return maxGold

        maximumGold = 0
        for r in range(rowLen):
            for c in range(columnLen):
                maximumGold = max(maximumGold, dfs(r, c, grid))
        return maximumGold
