# Last updated: 5/26/2025, 2:22:07 PM
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid) * len(grid)
        grid_set = set()

        res = []

        for row in grid:
            for num in row:
                if num in grid_set:
                    res.append(num)
                else:
                    grid_set.add(num)

        for i in range(1,n+1):
            if i not in grid_set:
                res.append(i)
        return res