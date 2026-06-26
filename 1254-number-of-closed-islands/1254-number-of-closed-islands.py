from collections import deque

class Solution:
    def traverse(self, grid, queue, visited):
        m = len(grid)
        n = len(grid[0])

        dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        is_closed_island = True
        
        while queue:
            i, j = queue.popleft()

            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                is_closed_island = False

            for di, dj in dirs:
                if 0 <= i+di < m and 0 <= j+dj < n and (i+di, j+dj) not in visited:
                    if grid[i+di][j+dj] == 0:
                        queue.append((i+di, j+dj))
                        visited.add((i+di, j+dj))
        
        return is_closed_island

    def closedIsland(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        queue = deque()
        visited = set()
        closed_island_count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and (i, j) not in visited:
                    queue.append((i, j))
                    visited.add((i, j))

                    if self.traverse(grid, queue, visited):
                        closed_island_count += 1
        
        return closed_island_count