# Last updated: 5/26/2025, 1:57:15 PM
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:

        n = len(mat)
        primary_sum = 0
        secondary_sum = 0

        for i in range(n):
            primary_sum += mat[i][i]

        for i in range(n):
            if i == n-i-1:
                continue
            else:
                secondary_sum += mat[i][n-i-1] 
        
        return primary_sum + secondary_sum
        