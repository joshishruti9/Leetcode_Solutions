class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid
                else:
                    low = mid + 1
            else:
                # target is to the right of mid
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid

        return low if nums[low] == target else -1
