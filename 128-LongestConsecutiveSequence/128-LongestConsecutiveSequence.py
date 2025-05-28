# Last updated: 5/27/2025, 7:27:00 PM
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        nums.sort()
        count = 0
        max_count = 0

        for i in range(len(nums)-1):
            if abs(nums[i+1] - nums[i]) == 1:
                count += 1
            elif abs(nums[i+1] - nums[i]) == 0:
                continue
            else:
                max_count = max(max_count, count)
                count = 0 

        max_count = max(max_count, count)
        return max_count+1
        