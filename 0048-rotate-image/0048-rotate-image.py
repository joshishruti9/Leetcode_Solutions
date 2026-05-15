class Solution:
    # We need to find number of frame(squares) in matrix -> count
    # We will call our transorm function count time
    # Inside transform function we will mobilise all the values together for that we need to find a starting and ending both row and column
    # Starting row and starting column will always be same and equal to curr_frame_num
    # For ending row and enging col both will be same equal to m-1-curr_frame_num
    # Now to transform/mobilise all values from one row we need to run loop for row_num times
    # We will mobilise them together to avoid extra variable
    # We need to find the postions

    # Time Complexity of this algorithm will be O(frame_count * m)
    # Space Complexity would be O(1)


    def transform(self, frame_num, matrix, m):
        sr = sc = frame_num
        er = ec = m - 1 - frame_num

        for i in range(ec-sc):
            matrix[sr+i][ec], matrix[er][ec-i], matrix[er-i][sc], matrix[sr][sc+i] = matrix[sr][sc+i], matrix[sr+i][ec], matrix[er][ec-i], matrix[er-i][sc]

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        framecount = 0
        m = len(matrix)
        
        framecount = math.ceil(m/2)

        for i in range(framecount):
            self.transform(i, matrix, m)
        