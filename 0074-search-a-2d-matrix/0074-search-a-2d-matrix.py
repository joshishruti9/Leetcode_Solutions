class Solution:
    def search(self, low, high, target, nums):
        
        while low < high:
            mid = (low + high) // 2

            if nums[mid] < target:
                low = mid+1
            else:
                high = mid
        
        return low 

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix)
        n = len(matrix[0])
        row = 0
        index = 0

        while row < m:
            if matrix[row][0] <= target and target <= matrix[row][n-1]:
                index = self.search(0, n-1, target, matrix[row])
                return matrix[row][index] ==  target
            
            row += 1

        return False