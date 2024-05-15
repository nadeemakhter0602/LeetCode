from collections import deque
import heapq


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        N = len(grid)

        def bfs(grid):
            q = deque()
            for r in range(N):
                for c in range(N):
                    if grid[r][c]:
                        q.append((1, r, c))
                        grid[r][c] = 0
            while q:
                dist, r, c = q.popleft()
                if r < 0 or c < 0 or r == N or c == N or grid[r][c] >= 1:
                    continue
                grid[r][c] = dist
                for r2, c2 in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    q.append((dist + 1, r2, c2))

        bfs(grid)
        maxHeap = [(-grid[0][0], 0, 0)]
        visited = set()
        while maxHeap:
            dist, r, c = heapq.heappop(maxHeap)
            if r < 0 or c < 0 or r == N or c == N or (r, c) in visited:
                continue
            visited.add((r, c))
            dist = min(-dist, grid[r][c])
            if (r, c) == (N - 1, N - 1):
                return dist - 1
            for r2, c2 in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                heapq.heappush(maxHeap, (-dist, r2, c2))
