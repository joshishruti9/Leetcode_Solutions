class Solution:
    def traverse(self, grid, queue, visited, m, n):
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        count = 0

        while queue:
            queue2 = []
            for i, j in queue:
                for di, dj in dirs:
                    if 0 <= i+di < m and 0 <= j+dj < n and (i+di, j+dj) not in visited and grid[i+di][j+dj] == 1:
                        grid[i+di][j+dj] = 2
                        queue2.append((i+di, j+dj))
                        visited.add((i+di, j+dj))
            
            count += 1
            queue = queue2

        return count

    def orangesRotting(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        queue = deque()
        visited = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                    visited.add((i, j))

        count = self.traverse(grid, queue, visited, m, n)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        
        return 0 if count == 0 else count-1
        