class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[m-1][n-1] == 1 or obstacleGrid[0][0] == 1:
            return 0

        mat = [[0 for j in range(n)] for i in range(m)]

        mat[m-1][n-1] = 1

        flag = False
        for i in range(m-2, -1, -1):
            if not flag and obstacleGrid[i][n-1] == 1:
                flag = True
            else:
                mat[i][n-1] = mat[i+1][n-1]
        
        flag = True
        for i in range(n-2, -1, -1):
            if flag and obstacleGrid[m-1][i] == 1:
                flag = False
            else:
                mat[m-1][i] = mat[m-1][i+1]


        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                if obstacleGrid[i][j] == 1:
                    mat[i][j] = 0
                else:
                    mat[i][j] = mat[i+1][j] + mat[i][j+1]

        return mat[0][0]
        