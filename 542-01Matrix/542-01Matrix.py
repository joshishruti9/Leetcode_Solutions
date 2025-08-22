# Last updated: 8/22/2025, 1:02:49 PM
from collections import deque
class Solution:
    def traverse(self, mat, visited, zeros, m, n, ans):
        queue = []
        count = 1
        dirs = [(-1,0),(0,-1),(0,1),(1,0)]

        while zeros:
            queue = []
            for i, j in zeros:
                for di, dj in dirs:
                    if 0 <= (i+di) < m and 0 <= (j+dj) < n and (i+di, j+dj) not in visited:
                        if mat[i+di][j+dj] == 1:
                            queue.append((i+di, j+dj))
                            visited.add((i+di, j+dj))
                            ans[i+di][j+dj] = count
            
            count += 1
            zeros = queue
            
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        m = len(mat)
        n = len(mat[0])
        ans = [[0 for i in  range(n)]for j in range(m)]
        zeros = deque()
        visited = set()
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    zeros.append((i,j))
                    visited.add((i,j))
     
        self.traverse(mat, visited, zeros, m, n, ans)

        return ans