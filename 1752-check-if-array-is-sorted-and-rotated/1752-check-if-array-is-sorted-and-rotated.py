class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0

        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                count += 1
            
        
        return True if (count == 0 or count == 1 and nums[0] >= nums[-1]) else False