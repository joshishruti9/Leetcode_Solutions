# Last updated: 6/18/2025, 9:39:06 PM
class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        m = len(grid)

        for i in range(m):
            for j in range(m):
                if i==j or j == m-1-i:
                    if grid[i][j] == 0:
                        return False
                else:
                    if grid[i][j] != 0:
                        return False
        return True
        