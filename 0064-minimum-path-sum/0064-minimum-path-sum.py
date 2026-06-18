class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        mat = [[0 for j in range(n)] for i in range(m)]

        mat[m-1][n-1] = grid[m-1][n-1]

        for i in range(n-2, -1, -1):
            mat[m-1][i] = grid[m-1][i] + mat[m-1][i+1]

        for i in range(m-2, -1, -1):
            mat[i][n-1] = mat[i+1][n-1] + grid[i][n-1]
        
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                mat[i][j] = min(mat[i+1][j], mat[i][j+1]) + grid[i][j]
        
        return mat[0][0]
                
        