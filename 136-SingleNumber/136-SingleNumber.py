# Last updated: 5/8/2025, 7:36:12 PM
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        num = nums[0]
        for i in range(1,len(nums)):
            num = num ^ nums[i]
        
        return num