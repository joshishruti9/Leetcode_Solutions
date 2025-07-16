# Last updated: 7/16/2025, 12:38:03 AM
class Solution:
    def find_last(self, nums, target, low, high):

        while low < high:
            mid = (low + high) // 2
            if nums[mid] <= target:
                low = mid + 1
            else:
                high = mid

        return high-1 if high > 0 and nums[high-1]==target else -1 

    def find_first(self, nums, target, low, high):
    
        while low < high:
            mid = (low + high) // 2

            if target <= nums[mid]:
                high = mid
            else:
                low = mid + 1

        print(low)
        return low if low < len(nums) and nums[low] == target else -1 
             

    def searchRange(self, nums: List[int], target: int) -> List[int]:

        n = len(nums)
        if n == 0:
            return [-1,-1]

        res1 = self.find_first(nums, target, 0, n)
        res2 = self.find_last(nums, target, 0, n)
        
        return [res1,res2]
        