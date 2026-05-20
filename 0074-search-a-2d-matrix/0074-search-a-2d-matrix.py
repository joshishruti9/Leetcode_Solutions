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
        count = 0
        index = 0

        for row in matrix:
            if row[0] <= target and target <= row[n-1]:
                index = self.search(0, n-1, target, row)
                return matrix[count][index] ==  target
            
            count += 1

        return False