class Solution:
    def jump(self, nums: List[int]) -> int:

        n = len(nums)
        memo = [float("inf")]*n

        memo[n-1] = 0


        for i in range(n-2, -1, -1):
            end = min(n-1, nums[i]+i)
            for j in range(i+1, end+1):
                memo[i] = min(memo[i], memo[j]+1)

        return memo[0]
        