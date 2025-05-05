# Last updated: 5/5/2025, 3:16:22 PM
from collections import deque

class Solution:
    def find_neighbours(self, grid, m, n, i, j, queue, visited):
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        for di, dj in directions:
            if 0 <= (i+di) < m and 0 <= (j+dj) < n and grid[i+di][j+dj] == 1 and (i+di,j+dj) not in visited:
                queue.append((i+di,j+dj))
                visited.add((i+di,j+dj))

    def traverse(self, grid, m, n, queue, visited):
        count = 0

        while queue:
            i,j = queue.popleft()
            self.find_neighbours(grid,m,n,i,j,queue,visited)
            count += 1
            
        self.max_area = max(self.max_area, count)    


    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.max_area = 0

        m = len(grid)
        n = len(grid[0])
        visited = set()
        queue = deque()

        for i in range(m):
            for j in range(n):
                if (i,j) not in visited and grid[i][j] == 1:
                    visited.add((i,j))
                    queue.append((i,j))
                    self.traverse(grid, m, n, queue, visited)

        return self.max_area