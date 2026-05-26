class Solution:
    def search_left(self, nums, low, high, target):

        while low < high:
            mid = (low + high) // 2

            if nums[mid] <= target:
                low = mid + 1
            else:
                high = mid
        
        return low

    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if len(nums) == 0:
            return [-1, -1]
        

        low = bisect.bisect_left(nums, target)
        high = bisect.bisect_right(nums, target)

        start = low if low < len(nums) and nums[low] == target else -1
        end = high-1 if nums[high-1] == target and start != -1 else -1

        
        return [start, end]
        