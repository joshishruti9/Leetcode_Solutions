class Solution:
    def bisect_left(self, nums, target):
        low = 0
        high = len(nums)-1

        while low < high:
            mid = (low + high) // 2

            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid
        
        return low
    
    def bisect_right(self, nums, target):
        low = 0
        high = len(nums)
        
        while low < high:
            mid = (low + high) // 2

            if nums[mid] <= target:
                low = mid + 1
            else:
                high = mid
        
        return high

    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if len(nums) == 0:
            return [-1, -1]
        

        low = self.bisect_left(nums, target)
        high = self.bisect_right(nums, target)

        start = low if low < len(nums) and nums[low] == target else -1
        end = high-1 if high > 0 and nums[high-1] == target else -1

        
        return [start, end]
        