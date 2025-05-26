# Last updated: 5/26/2025, 1:51:24 PM
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:

        n = len(grid)

        res = [[0 for col in range(n-2)] for row in range(n-2)]
        r= c = 0

        for i in range(0, n-2):
            for j in range(0, n-2):
                max_row1 = max(grid[i][j:j+3])
                max_row2 = max(grid[i+1][j:j+3])
                max_row3 = max(grid[i+2][j:j+3])

                res[i][j] = max(max_row1, max_row2, max_row3)
        
        return res