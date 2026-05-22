class Solution:
    def traverse(self, grid, m, n, queue, visited):

        dirs = [(0,-1),(-1,0),(1,0),(0,1)]
        count = 0

        while queue:
            i, j = queue.popleft()

            for di, dj in dirs:
                if 0 <= i+di < m and 0 <= j+dj < n and grid[i+di][j+dj] == 1:
                    if (i+di, j+dj) not in visited:
                        queue.append((i+di, j+dj))
                        visited.add((i+di, j+dj))
                else:
                    count += 1
        
        return count
        
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        queue = deque()
        visited = set()
        count = 0
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i,j))
                    visited.add((i,j))
                    count = self.traverse(grid, m, n, queue, visited)
                    return count

        return count
        