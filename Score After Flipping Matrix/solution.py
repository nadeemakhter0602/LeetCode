class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        rowLen = len(grid)
        columnLen = len(grid[0])

        def flipRow(r, grid):
            for c in range(columnLen):
                grid[r][c] = 0 if grid[r][c] == 1 else 1

        def flipColumn(c, grid):
            for r in range(rowLen):
                grid[r][c] = 0 if grid[r][c] == 1 else 1

        # flip rows with first element 0
        for r in range(rowLen):
            if grid[r][0] == 0:
                flipRow(r, grid)
        # flip columns where number of 0s are more than 1s
        for c in range(1, columnLen):
            counts = [0, 0]
            for r in range(rowLen):
                if grid[r][c] == 0:
                    counts[0] += 1
                else:
                    counts[1] += 1
            if counts[0] > counts[1]:
                flipColumn(c, grid)
        # calculate final score
        score = 0
        for r in range(rowLen):
            number = 0
            for c in range(columnLen):
                number += 2 ** (columnLen - c - 1) * grid[r][c]
            score += number
        return score
