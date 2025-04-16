# Last updated: 4/16/2025, 1:16:29 PM
class Solution:
    def dp(self, i, j, grid, m, n):
        if (i,j) not in self.memo:
            if i < m-1:
                op1 = self.dp(i+1,j,grid,m,n)
            else:
                op1 = float("inf")

            if j < n-1:
                op2 = self.dp(i,j+1,grid,m,n)
            else:
                op2 = float("inf")

            self.memo[(i,j)] = grid[i][j] + min(op1,op2)
        
        return self.memo[(i,j)]

    def minPathSum(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        self.memo = {}
        self.memo[(m-1,n-1)] = grid[m-1][n-1]
        self.dp(0,0,grid,m,n)

        return self.memo[(0,0)]

        