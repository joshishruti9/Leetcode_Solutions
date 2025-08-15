# Last updated: 8/14/2025, 6:08:17 PM
class Solution:
    def dp(self, row_index, col_index, triangle, n):
        if (row_index, col_index) in self.memo:
            return self.memo[(row_index, col_index)]
        
        next_row_index = row_index + 1
        next_col_index = col_index

        min_val = min(self.dp(next_row_index, next_col_index, triangle, n), self.dp(next_row_index, next_col_index+1, triangle, n))
        self.memo[(row_index, col_index)] = min_val + triangle[row_index][col_index]

        return self.memo[(row_index, col_index)]

    def minimumTotal(self, triangle: List[List[int]]) -> int:

        n = len(triangle)
        self.memo = {}

        for i, num in enumerate(triangle[n-1]):
            self.memo[(n-1, i)] = num

        print(self.memo)
        val = triangle[0][0]
        self.dp(0, 0, triangle, n)

        return self.memo[(0,0)]