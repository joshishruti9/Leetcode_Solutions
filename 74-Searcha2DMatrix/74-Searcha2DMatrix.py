# Last updated: 5/30/2025, 1:20:47 PM
class Solution:
    def bisect_left(self, arr, low, high, target):

        while low < high:
            mid = (low + high) // 2
            if arr[mid] < target:
                low = mid + 1
            else:
                high = mid
        
        return low

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix)
        n = len(matrix[0])
        count = 0

        for row in matrix:
            if target >= row[0] and target <= row[n-1]:
                index = self.bisect_left(row, 0, n, target)
                if matrix[count][index] == target:
                    return True
                else:
                    return False
            count += 1
        
        return False