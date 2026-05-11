from collections import deque
class Solution:
    def getNeighbours(self,grid,i,j,m,n,queue,visited):
        
        directions = {(0,1),(0,-1),(-1,0),(1,0)}
        
        for di, dj in directions:
            if 0 <= i + di < m and 0 <= j + dj < n and grid[i+di][j+dj] == '1' and (i+di,j+dj) not in visited:
                queue.append((i+di,j+dj))
                visited.add((i+di,j+dj))

    def findIsland(self,grid,m,n,queue,visited):
        while queue:
            i, j = queue.popleft()
            self.getNeighbours(grid,i,j,m,n,queue,visited)

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = set()
        queue = deque()
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i,j) not in visited:
                    queue.append((i,j))
                    visited.add((i,j))
                    self.findIsland(grid,m,n,queue,visited)
                    count += 1
        return count