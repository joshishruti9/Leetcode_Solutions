class Solution:
    def search(self, low, high, nums):

        while low < high:
            mid = (low + high) // 2

            print(mid)

            if (nums[mid-1] < nums[mid] > nums[mid+1]) or (mid == 0 and nums[mid+1] < nums[mid]) or (mid == len(nums)-1 and nums[mid-1] < nums[mid]):
                return mid
            elif nums[mid+1] > nums[mid]:
                low = mid+1
            else:
                high = mid
        
        return low

    def findPeakElement(self, nums: List[int]) -> int:

        start = 0
        end = len(nums)

        return self.search(start, end-1, nums)