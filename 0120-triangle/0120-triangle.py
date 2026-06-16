class Solution:
    def traverse(self, triangle, row_num, col_num):

        if (row_num, col_num) in self.memo:
            return self.memo[(row_num, col_num)]
        
        curr_val = triangle[row_num][col_num]
        min_sum = curr_val + min(self.traverse(triangle, row_num+1, col_num), self.traverse(triangle, row_num+1, col_num+1))
        self.memo[(row_num, col_num)] = min_sum
        return self.memo[(row_num, col_num)]

    def minimumTotal(self, triangle: List[List[int]]) -> int:

        self.memo = {}
        n = len(triangle)

        for index, num in enumerate(triangle[n-1]):
            self.memo[(n-1, index)] = num
        
        return self.traverse(triangle, 0, 0)
