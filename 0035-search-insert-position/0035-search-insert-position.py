class Solution:
    def search(self, nums, low, high, target):

        while low < high:
            mid = (low + high) // 2

            if target <= nums[mid]:
                high = mid
            else:
                low = mid + 1
        
        return low

    def searchInsert(self, nums: List[int], target: int) -> int:

        return self.search(nums, 0, len(nums), target)
        