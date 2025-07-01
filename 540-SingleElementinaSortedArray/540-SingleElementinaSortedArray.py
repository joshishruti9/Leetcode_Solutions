# Last updated: 6/30/2025, 8:42:25 PM
class Solution:
    def binary(self, nums, low, high):

        while low < high:
            mid = (low + high) // 2
            if mid % 2 == 0:
                if nums[mid] != nums[mid+1]:
                    high = mid
                else:
                    low = mid + 1
            else:
                if nums[mid] != nums[mid+1]:
                    low = mid + 1
                else:
                    high = mid
                
        return nums[low]

    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)

        if len(nums) == 1:
            return nums[0]

        return self.binary(nums, 0, n-1)