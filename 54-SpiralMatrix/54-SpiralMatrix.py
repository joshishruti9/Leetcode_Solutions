# Last updated: 3/23/2025, 2:06:36 PM
import math
class Solution:
    def traverse_spiral(self, spiral_count, row_nums, col_nums, output, matrix):
        sr = sc = spiral_count
        er = row_nums - spiral_count - 1 # excluding
        ec = col_nums - spiral_count - 1 # excluding

        if sr == er and sc == ec:
            output.append(matrix[sr][sc])
            return

        if sr == er:
            for j in range(sc,ec+1):
                output.append(matrix[sr][j])
            return
        
        if sc == ec:
            for i in range(sr,er+1):
                output.append(matrix[i][sc])
            return

        for j in range(sc, ec):
            output.append(matrix[sr][j])

        for i in range(sr, er):
            output.append(matrix[i][ec])
        
        for j in range(ec,sc,-1):
            output.append(matrix[er][j])
        
        for i in range(er,sr,-1):
            output.append(matrix[i][sc]) 

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        row_nums = len(matrix)
        col_nums = len(matrix[0])
        output = []

        print(row_nums, " ",col_nums)

        spiral_count = min(row_nums, col_nums) / 2
        spiral_count = math.ceil(spiral_count)

        for i in range(spiral_count):
            self.traverse_spiral(i,row_nums,col_nums,output,matrix)

        return output

        