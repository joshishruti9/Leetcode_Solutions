# Last updated: 8/6/2025, 1:42:40 PM
class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        ans = []

        for i in range(n):
            max_len = 0
            for j in range(m):
                max_len = max(max_len, len(str(grid[j][i])))
            
            ans.append(max_len)
        
        return ans