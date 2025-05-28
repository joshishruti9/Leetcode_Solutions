# Last updated: 5/28/2025, 4:17:17 PM
class Solution:
    def bisect_left(self, nums, low, high, target):

        while low < high:
            mid = (high + low) // 2

            if nums[mid] == target:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high-1]:
                    low = mid + 1
                else:
                    high = mid

        return low
            
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        index = self.bisect_left(nums, 0, n, target)

        if index < len(nums) and nums[index] == target:
            return index
        
        return -1
        