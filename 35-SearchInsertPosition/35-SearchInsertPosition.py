# Last updated: 4/23/2025, 4:09:26 PM
class Solution:
    def bisect_left(self, low, high, target, nums):

        while low < high:
            mid = (low+high) // 2
            if target <= nums[mid]:
                high = mid
            else:
                low = mid + 1


        return low
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.bisect_left(0,len(nums),target,nums)
        