# Last updated: 4/18/2025, 12:48:07 PM
class Solution:
    def dp(self, index, nums):
        min_jump = float("inf")

        if index not in self.memo:
            for i in range(1, nums[index]+1):
                if index + i < len(nums):
                    min_jump = min(min_jump, self.dp(index+i, nums))
            
            self.memo[index] = min_jump + 1

        return self.memo[index]
        
    def jump(self, nums: List[int]) -> int:

        self.memo = {}
        n = len(nums)
        self.memo[n-1] = 0

        self.dp(0,nums)

        return self.memo[0]
        