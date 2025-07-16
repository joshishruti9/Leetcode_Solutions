# Last updated: 7/15/2025, 11:59:30 PM
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        start = -1
        end = -1

        for i in range(len(nums)):
            if nums[i] == target and start == -1:
                start = i
                end = i
            elif nums[i] == target and start != -1:
                end = i
        
        return [start,end]
        