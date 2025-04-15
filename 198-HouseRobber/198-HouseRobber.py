# Last updated: 4/14/2025, 8:29:33 PM
class Solution:
    def dp(self, k, nums):
        if k not in self.memo:
            self.memo[k] = max((nums[k] + self.dp(k+2, nums)), self.dp(k+1, nums))
        
        return self.memo[k]

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])

        self.memo = {}
        n = len(nums)
        self.memo[n-1] = nums[n-1]
        self.memo[n-2] = max(nums[n-1],nums[n-2])
        max_amount = self.dp(0, nums)

        return max_amount       