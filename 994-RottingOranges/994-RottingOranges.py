# Last updated: 8/22/2025, 1:17:22 PM
class Solution:
    def find_neighbours(self, queue, visited, m, n, i, j, grid):
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        for di, dj in dirs:
            if 0 <= i+di < m and 0 <= j+dj < n and (i+di, j+dj) not in visited:
                if grid[i+di][j+dj] == 1:
                    queue.append((i+di,j+dj))
                    visited.add((i+di, j+dj))
                    grid[i+di][j+dj] = 2

    def traverse(self, grid, rotten, visited, m, n):
        queue = []
        count = 0
        while rotten:
            queue = []
            for i, j in rotten:
                self.find_neighbours(queue, visited, m, n, i, j, grid)
            count += 1
            rotten = queue
        return max(0,count - 1)

    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        rotten = []
        visited = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten.append((i,j))
                    visited.add((i,j))

        count = self.traverse(grid, rotten, visited, m, n)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        
        return count
        