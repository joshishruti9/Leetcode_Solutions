# Last updated: 7/30/2025, 2:41:35 PM
class Solution:
    def binary_search(self, nums, low, high, target):

        while low < high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid
                else:
                    low = mid + 1         
            else:
                if nums[high-1] >= target > nums[mid]:
                    low = mid + 1
                else:
                    high = mid
        
        return low
           

    def search(self, nums: List[int], target: int) -> int:

        index = self.binary_search(nums, 0, len(nums), target)
        print(index)
        
        if index < len(nums) and nums[index] == target:
            return index
        
        return -1
        