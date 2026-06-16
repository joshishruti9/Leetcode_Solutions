class Solution:
    def dp(self, nums, curr_index):
        if curr_index in self.memo:
            return self.memo[curr_index]
        
        max_amount = max(nums[curr_index] + self.dp(nums, curr_index+2), self.dp(nums, curr_index+1))
        self.memo[curr_index] = max_amount
        return self.memo[curr_index]

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        self.memo = {}

        self.memo[n-1] = nums[n-1]
        self.memo[n-2] = max(nums[n-1], nums[n-2])

        return self.dp(nums, 0)


        