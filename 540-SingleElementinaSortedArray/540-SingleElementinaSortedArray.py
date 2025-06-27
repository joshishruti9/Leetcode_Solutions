# Last updated: 6/27/2025, 1:32:32 AM
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        output = 0
        i = 0
        n = len(nums)

        while i < (n-2):
            if nums[i] == nums[i+1]:
                i += 2
            else:
                return nums[i]
        
        return nums[n-1]