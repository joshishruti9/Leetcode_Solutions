class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = [False] * n

        memo[n-1] = True

        for i in range(n-2, -1, -1):
            flag = False
            for j in range(nums[i]+1):
                flag = flag or memo[i+j]
                if flag:
                    break
            memo[i] = flag
        
        return memo[0]
        