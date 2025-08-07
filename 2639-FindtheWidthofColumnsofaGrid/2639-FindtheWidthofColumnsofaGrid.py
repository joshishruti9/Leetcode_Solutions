# Last updated: 8/7/2025, 12:03:53 PM
class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        ans = []

        for i in range(n):
            max_len = 0
            for row in grid:
                max_len = max(max_len, len(str(row[i])))
            
            ans.append(max_len)
        
        return ans