from collections import deque
class Solution:
    def traverse(self, grid, queue, visited, m, n):
        count = 0
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        queue2 = []
        

        while queue:
            queue2 = []
            for i, j in queue:
                for di, dj in dirs:
                    if 0 <= i+di < m and 0 <= j+dj < n and (i+di, j+dj) not in visited and grid[i+di][j+dj] == 1:
                        visited.add((i+di, j+dj))
                        queue2.append((i+di, j+dj))
                        grid[i+di][j+dj] = 2

            queue = queue2   
            count += 1
        

        return count

            


    def orangesRotting(self, grid: List[List[int]]) -> int:

        queue = deque()
        visited = set()
        m = len(grid)
        n = len(grid[0])


        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j))
                    visited.add((i,j))
        
        count = self.traverse(grid, queue, visited, m, n)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        
        return max(0,count - 1)

        
        