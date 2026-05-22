class Solution:
    def bisect_left(self, low, high, nums, target):
        
        while low < high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            
            #check whether left half is sorted or not?
            if nums[mid] >= nums[low]:
                if nums[low] <= target < nums[mid]:
                    high = mid
                else:
                    low = mid + 1
            
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid
                
        return low

            
    def search(self, nums: List[int], target: int) -> int:

        index = self.bisect_left(0, len(nums)-1, nums, target)
        return index if nums[index] == target else -1
        