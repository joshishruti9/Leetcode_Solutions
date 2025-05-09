# Last updated: 5/8/2025, 7:33:20 PM
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_one = 0
        count = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                max_one = max(max_one,count)
                count = 0
        
        max_one = max(max_one,count)
        return max_one
        