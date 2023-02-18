class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def explore(grid, i, j, visited):
            if not(i >= 0 and i < len(grid)):
                return 0
            if not(j >= 0 and  j < len(grid[0])):
                return 0
            if grid[i][j] == "0":
                return 0
            if (i,j) in visited:
                return 0
            visited.add((i, j))
            explore(grid, i-1, j, visited)
            explore(grid, i+1, j, visited)
            explore(grid, i, j-1, visited)
            explore(grid, i, j+1, visited)
            return 1
        total = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                total += explore(grid, i, j, visited)
        return total