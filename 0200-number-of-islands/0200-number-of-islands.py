from queue import deque

class Solution:
    def find_neighbours(self, i, j, grid, m, n, queue, visited):
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]

        for di, dj in dirs:
            if 0 <= i+di < m and 0 <= j+dj < n and (i+di, j+dj) not in visited and grid[i+di][j+dj] == '1' :
                queue.append((i+di,j+dj))
                visited.add((i+di, j+dj))
    
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        queue = deque()
        visited = set()

        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i,j) not in visited:
                    queue.append((i,j))
                    visited.add((i,j))
                    while queue:
                        r, c = queue.popleft()
                        self.find_neighbours(r, c, grid, m, n, queue, visited)

                    count += 1

        return count
        