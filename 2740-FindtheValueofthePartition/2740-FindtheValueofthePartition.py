# Last updated: 8/9/2025, 10:28:50 PM
class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:

        nums.sort()
        min_diff = float("inf")

        for i in range(1, len(nums)):
            min_diff = min(min_diff, nums[i] - nums[i-1])
        
        return min_diff
        