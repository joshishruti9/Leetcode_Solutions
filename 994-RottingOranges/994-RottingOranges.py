# Last updated: 3/27/2025, 9:45:56 PM
from collections import deque
class Solution:
    def traverse(self, visited, m, n, grid, rotten):
        count = 0
        rot_flag = False
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        while rotten:
            queue = []
            for i,j in rotten:
                for di, dj in directions:
                    if 0 <= (i+di) < m and 0 <= (j+dj) < n and ((i+di, j+dj)) not in visited and grid[i+di][j+dj] == 1:
                        grid[i+di][j+dj] = 2
                        queue.append((i+di,j+dj))
                        visited.add((i+di,j+dj))
            count += 1
            rotten = queue 
        return max(count-1,0)

    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = set()
        rotten = deque()
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten.append((i,j))
                    visited.add((i,j))

        count = self.traverse(visited, m, n, grid, rotten)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1

        return count
