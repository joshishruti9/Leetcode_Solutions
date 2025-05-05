# Last updated: 5/5/2025, 4:06:50 PM
class Solution:
    def bisect_left(self, nums, low, high):

        while low < high:
            mid = (low+high) // 2
            if nums[mid] < nums[mid+1] and nums[mid] < nums[high]:
                high = mid
            else:
                low = mid+1
        
        return low

    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        index = self.bisect_left(nums, 0, n-1)

        if index == 0 and nums[index] > nums[n-1]:
            return nums[n-1]
     
        return nums[index]